# 417. Pacific Atlantic Water Flow

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/pacific-atlantic-water-flow/

## Task

An island is drawn as an `m x n` grid `heights`, where `heights[r][c]` is the height of the cell
in row `r` and column `c`. The Pacific Ocean touches the top edge and the left edge of the island.
The Atlantic Ocean touches the bottom edge and the right edge.

Rain water in a cell can flow to a neighbouring cell above, below, left or right of it when that
neighbour's height is less than or equal to the current cell's height. Water in a cell on an edge
can flow into the ocean that touches that edge.

Return the list of all cells `[r, c]` from which water can reach both the Pacific and the
Atlantic. The cells can be listed in any order.

## Examples

**Example 1**

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

Some of the paths:

```
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
```

Other cells, and other paths for these cells, are possible.

**Example 2**

```
Input: heights = [[1]]
Output: [[0,0]]
```

The only cell touches both oceans.

## Constraints

- `m == heights.length`
- `n == heights[r].length`
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`

## Target complexity

O(m * n) time and O(m * n) space.

## Hints

<details><summary>Hint 1</summary>

Following the water from every cell separately repeats a lot of work on a 200 x 200 grid. Is
there a small set of cells where every successful path ends?

</details>

<details><summary>Hint 2</summary>

Think about the direction of the question. Instead of asking where water from one cell can go,
ask which cells can send water to a given cell.

</details>

<details><summary>Hint 3</summary>

Handle each ocean on its own first. How do you combine the two results?

</details>
