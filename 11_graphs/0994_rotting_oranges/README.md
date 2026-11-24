# 994. Rotting Oranges

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/rotting-oranges/

## Task

You get an `m x n` grid `grid` where each cell holds one of three values:

- `0`: an empty cell,
- `1`: a fresh orange,
- `2`: a rotten orange.

Every minute, each fresh orange that is directly above, below, left or right of a rotten orange
becomes rotten.

Return the smallest number of minutes after which no cell holds a fresh orange. If some fresh
orange can never become rotten, return `-1`.

## Examples

**Example 1**

```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
```

**Example 2**

```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
```

The orange in the bottom-left corner (row 2, column 0) never becomes rotten: its only neighbours
are empty cells, and rotting does not spread diagonally.

**Example 3**

```
Input: grid = [[0,2]]
Output: 0
```

There are no fresh oranges at minute 0, so the answer is 0.

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`.

## Target complexity

O(m * n) time and O(m * n) space.

## Hints

<details><summary>Hint 1</summary>

All rotten oranges spread at the same time. Which oranges become rotten in minute 1? Which ones
in minute 2?

</details>

<details><summary>Hint 2</summary>

Count the fresh oranges at the start. How does that count help you decide between the number of
minutes and `-1`?

</details>

<details><summary>Hint 3</summary>

A grid with no fresh oranges at all needs 0 minutes, even if it has no rotten oranges either.

</details>
