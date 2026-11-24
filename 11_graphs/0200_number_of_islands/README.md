# 200. Number of Islands

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/number-of-islands/

## Task

You get an `m x n` grid `grid` of characters, where `'1'` is land and `'0'` is water. Return the
number of islands.

An island is a group of land cells joined to each other by steps up, down, left or right (not
diagonally). Everything outside the grid counts as water.

## Examples

**Example 1**

```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

**Example 2**

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`.

## Target complexity

O(m * n) time and O(m * n) space.

## Hints

<details><summary>Hint 1</summary>

When you find a land cell, how can you make sure that no other cell of the same island is counted
again later?

</details>

<details><summary>Hint 2</summary>

Every land cell belongs to exactly one island. Each island needs to be counted once, at the first
of its cells that you reach.

</details>

<details><summary>Hint 3</summary>

The cells are characters: compare with `"1"`, not with the number `1`.

</details>
