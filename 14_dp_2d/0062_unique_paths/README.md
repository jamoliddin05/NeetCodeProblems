# 62. Unique Paths

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/unique-paths/

## Task

A robot stands in the top-left cell of a grid with `m` rows and `n` columns. With each move it
goes one cell down or one cell right.

Return the number of different paths that bring the robot to the bottom-right cell.

The tests are built so that the answer is at most `2 * 10^9`.

## Examples

**Example 1**

```
Input: m = 3, n = 7
Output: 28
```

**Example 2**

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

## Constraints

- `1 <= m, n <= 100`

## Hints

<details><summary>Hint 1</summary>

On its last move, from which cells can the robot enter the bottom-right cell?

</details>

<details><summary>Hint 2</summary>

The number of paths to any cell depends only on the numbers of paths to the cells it can be entered from.

</details>

<details><summary>Hint 3</summary>

Many different paths pass through the same cell. Does the count for that cell need to be worked out more than once?

</details>
