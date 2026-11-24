# 221. Maximal Square

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/maximal-square/

## Task

You get an `m x n` grid `matrix` in which every cell holds the character `"1"` or `"0"` (strings,
not numbers).

Find the largest square block of cells that contains only `"1"` cells and return its area, which is
the number of cells in it. If the grid has no `"1"` at all, return `0`.

## Examples

**Example 1**

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
```

**Example 2**

```
Input: matrix = [["0","1"],["1","0"]]
Output: 1
```

**Example 3**

```
Input: matrix = [["0"]]
Output: 0
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 300`
- `matrix[i][j]` is `'0'` or `'1'`.

## Hints

<details><summary>Hint 1</summary>

Suppose a cell is the bottom-right corner of a square of `"1"` cells with side `k`. What does that tell you about the cell to its left, the cell above it, and the cell diagonally above-left?

</details>

<details><summary>Hint 2</summary>

Checking every possible square cell by cell is far too slow for a 300 x 300 grid. Can the answer for one cell reuse the answers for cells next to it?

</details>

<details><summary>Hint 3</summary>

The grid holds the strings `"1"` and `"0"`, not the numbers `1` and `0`.

</details>
