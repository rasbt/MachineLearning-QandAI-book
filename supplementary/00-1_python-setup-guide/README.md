# Python Setup Tips



There are several different ways you can install Python and set up your computing environment. Here, I am illustrating my personal preference. 

(I am using computers running macOS, but this workflow is similar for Linux machines and may work for other operating systems as well.)



## 1. Download and install Miniforge

Download miniforge from the GitHub repository [here](https://github.com/conda-forge/miniforge).

<img src="figures/download.png" alt="download" style="zoom:33%;" />

Depending on your operating system, this should download either an `.sh` (macOS, Linux) or `.exe` file (Windows). 

For the `.sh` file, open your command line terminal and execute the following command

```bash
sh ~/Desktop/Miniforge3-MacOSX-arm64.sh
```

where `Desktop/` is the folder where the Miniforge installer was downloaded to. On your computer, you may have to replace it with `Downloads/`.

<img src="figures/miniforge-install.png" alt="miniforge-install" style="zoom:33%;" />

Next, step through the download instructions, confirming with "Enter".

## 2. Create a new virtual environment

After the installation was successfully completed, I recommend creating a new virtual environment called `dl-fundamentals`, which you can do by executing

```bash
conda create -n book python=3.9
```

<img src="figures/new-env.png" alt="new-env" style="zoom:33%;" />

Next, activate your new virtual environment (you have to do it every time you open a new terminal window or tab):

```bash
conda activate book
```



## Optional: styling your terminal

If you want to style your terminal similar to mine so that you can see which virtual environment is active,  check out the [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh) project.



# 3. Install new Python libraries



To install new Python libraries, you can now use the `conda` package installer. For example, you can install [JupyterLab](https://jupyter.org/install) and [watermark](https://github.com/rasbt/watermark) as follows:

```bash
conda install jupyterlab watermark
```



Alternatively you can also use `pip` to install libraries instead. By default, `pip` should be linked to your new `book` conda environment:

```bash
pip install jupyterlab watermark
```


---




Any questions? Please feel free to reach out in the [Discussion Forum](https://github.com/rasbt/MachineLearning-QandAI-book/discussions).