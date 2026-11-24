# 73. Set Matrix Zeroes

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/set-matrix-zeroes/

## Task

You get an `m x n` integer matrix. For every element that is `0`, set its whole row and its whole
column to `0`.

Only the zeros that are in the matrix at the start count: a zero you write does not make its own
row and column zero.

Do it in place: change `matrix` itself. The method returns nothing; the tests look at `matrix`
after the call.

## Examples

**Example 1**

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

**Example 2**

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## Constraints

- `m == matrix.length`
- `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

## Follow-up

- A solution with O(mn) extra space is easy, and probably not a good answer.
- O(m + n) extra space is better, but still not the best.
- Can you do it with O(1) extra space?

## Hints

<details><summary>Hint 1</summary>

If you write zeros while you are still looking for zeros, you can't tell a zero that was there from
one you wrote. Find out everything you need before you change anything.

</details>

<details><summary>Hint 2</summary>

To finish the job you don't need to remember where each zero is. What do you need to remember?

</details>

<details><summary>Hint 3</summary>

For O(1) extra space: is there a place inside the matrix itself where that information could be
kept? What would be lost if you wrote it there, and how can you save that first?

</details>
