import os
import sys
import tarfile
import time

import numpy as np
import pandas as pd
from packaging import version
from torch.utils.data import Dataset
from tqdm import tqdm
import urllib


def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = progress_size / (1024.0**2 * duration)
    percent = count * block_size * 100.0 / total_size

    sys.stdout.write(
        f"\r{int(percent)}% | {progress_size / (1024.**2):.2f} MB "
        f"| {speed:.2f} MB/s | {duration:.2f} sec elapsed"
    )
    sys.stdout.flush()


def download_dataset():
    source = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
    target = "aclImdb_v1.tar.gz"

    if os.path.exists(target):
        os.remove(target)

    if not os.path.isdir("aclImdb") and not os.path.isfile("aclImdb_v1.tar.gz"):
        urllib.request.urlretrieve(source, target, reporthook)

    if not os.path.isdir("aclImdb"):

        with tarfile.open(target, "r:gz") as tar:
            tar.extractall()


def load_dataset_into_to_dataframe():
    basepath = "aclImdb"

    labels = {"pos": 1, "neg": 0}

    df = pd.DataFrame()

    with tqdm(total=50000) as pbar:
        for s in ("test", "train"):
            for l in ("pos", "neg"):
                path = os.path.join(basepath, s, l)
                for file in sorted(os.listdir(path)):
                    with open(os.path.join(path, file), "r", encoding="utf-8") as infile:
                        txt = infile.read()

                    if version.parse(pd.__version__) >= version.parse("1.3.2"):
                        x = pd.DataFrame(
                            [[txt, labels[l]]], columns=["review", "sentiment"]
                        )
                        df = pd.concat([df, x], ignore_index=False)

                    else:
                        df = df.append([[txt, labels[l]]], ignore_index=True)
                    pbar.update()
    df.columns = ["text", "label"]

    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))

    print("Class distribution:")
    np.bincount(df["label"].values)

    return df


def partition_dataset(df):
    df_shuffled = df.sample(frac=1, random_state=1).reset_index()

    df_train = df_shuffled.iloc[:35_000]
    df_val = df_shuffled.iloc[35_000:40_000]
    df_test = df_shuffled.iloc[40_000:]

    df_train.to_csv("train.csv", index=False, encoding="utf-8")
    df_val.to_csv("val.csv", index=False, encoding="utf-8")
    df_test.to_csv("test.csv", index=False, encoding="utf-8")


class IMDBDataset(Dataset):
    def __init__(self, dataset_dict, partition_key="train"):
        self.partition = dataset_dict[partition_key]

    def __getitem__(self, index):
        return self.partition[index]

    def __len__(self):
        return self.partition.num_rows