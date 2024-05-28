# Errata


#### Chapter 8

The following sentence in Chapter 8

> Transformers are easy to parallelize because they take a fixed-length sequence of word or image tokens as input.

Is misleading because we only work with fixed-size sequences specifically during pretraining, finetuning, and batched inference. I.e., where we collect multiple sequences in a batch. A better explanation could be the following:

> Like other deep learning architectures, transformers facilitate parallelization in batch training by handling sequences of word or image tokens. Although they can process variable-length sequences, in practice, sequences are often padded or truncated to fixed lengths for efficient parallel computation across multiple sequences.