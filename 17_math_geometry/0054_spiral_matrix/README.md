# 54. Spiral Matrix

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/spiral-matrix/

## Task

You get an `m x n` matrix. Return all of its elements in spiral order.

Spiral order starts at the top-left corner and goes clockwise around the edge: right along the top
row, down the right column, left along the bottom row and up the left column. Then it does the same
with the part of the matrix that is still left inside, and so on until every element has been
taken exactly once.

## Examples

**Example 1**

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
```

**Example 2**

```
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Hints

<details><summary>Hint 1</summary>

Keep track of which rows and which columns have not been read yet. What changes after you finish
one side?

</details>

<details><summary>Hint 2</summary>

Try your idea by hand on a single row, on a single column and on a 3 x 5 matrix. What is left in
the middle of the 3 x 5 one, and is each of its elements read exactly once?

</details>
