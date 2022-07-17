# Weird Algorithm
A sequence of integers X is called weird if X[i + 1] > X[i] for all odd numbers i and X[i + 1] < X[i] otherwise. Provide an efficient algorithm to, given a sequence of n integers, find a weird subsequence with maximum number of integers. Note that there are at most 2n different subsequences (including the empty subsequence) of a sequence of n integers.

## Thinking about the Problem
Imagine that each point is a node, and that the edge which connects the node is coloured based on N1 - N2. 
When N1 > N2, the edge is Positive Color. q
When N1 < N1, the edge is Negative Color. 
When N1 == N2, the edge is No Color. 

The maximum weird subsequence is the maximum subsequence of Edges which switch between Positive and Negative. 
Every weird subsequence is either contained in a larger weird subsequence, or is the local largest weird subsequence. 
A local largest weird subsequence is one where no edges can be added on either side and keep the weirdness. 

## The Algorithm
As you travel across the path, record the current local largest weird subsequence, replacing the global largest weird subsequence when you find one larger than the previous. After one walk, without moving backwards, you will have found the maximum weird subsequence. 