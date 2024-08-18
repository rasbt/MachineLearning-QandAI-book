# Errata


#### Chapter 8

The following sentence in Chapter 8

> Transformers are easy to parallelize because they take a fixed-length sequence of word or image tokens as input.

Is misleading because we only work with fixed-size sequences specifically during pretraining, finetuning, and batched inference. I.e., where we collect multiple sequences in a batch. A better explanation could be the following:

> Like other deep learning architectures, transformers facilitate parallelization in batch training by handling sequences of word or image tokens. Although they can process variable-length sequences, in practice, sequences are often padded or truncated to fixed lengths for efficient parallel computation across multiple sequences.

#### Chapter 12

On the first page, just above the first figure (12-1), it says "two input and four output units" but should be "four inputs and two outputs" to match the figure caption of Figure 12-1.


#### Chapter 17

(p109) In figure 17-3, "next-sentence prediction" should be "next-word prediction".

#### Chapter 18

(p121, p122) In figure 18-6 and 18-7, "Fully connected layer" box that follows "Multihead self-attention" box should be removed.

#### Chapter 19

(p129) in the 2nd row of the second equation, that $\sum$ should be removed.

(p129, 132) 2nd line from the bottom, "q15-text-augment subfolder" should be "q19-evaluation-llms subfolder"
