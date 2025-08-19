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

#### Chapter 25

(p166) In note `stats.zscore` should be `stats.norm.ppf`.

#### Chapter 27

(p180) Below Figure 27-2, "AB", "BC", "AC" shoule be "A", "B", "C" respectively.

(p181) In thrid paragraph, "How about the second criterion" should be "How about the second part of the first criterion".

(p182) 4th and 9th line from the bottom, ">=" should be "<=". To correct the example, "p=0.5" should be changed, for example "p=0.1".

#### Chapter 28

(p188) In Exercise 28-1, "1(99 percent)" should be "1(100 percent)".

#### Chapter 30

(p194) 2nd line below Transfer Learning, "pretrained target dataset" should be "pretrained model on a target dataset".

(p203) In Figure 30-11, "label more training" should be "label more training data".

#### Appendix: Answer to the Exercises

(p208) In 3-1, in the last line, "example per class" is better than "example per image".

(p212) In last sentence of 10-2 answer, "deterministic dropout" should be "random dropout".

(p217) In first and last sentences of 20-2 answer, "stateful retraining" should be "stateful training".

(p209) In 4-2, the part about zero weights is wrong; it should say "gradients" and not "weights":

> While ReLU activations do not directly cause sparse weights, the zero activation outputs sometimes lead to zero weights that are not recoverable.

A better phrasing is:

> While ReLU activations do not directly cause sparse weights, zero activation outputs can lead to zero gradients, which in turn freeze the weights (i.e., prevent them from updating).


