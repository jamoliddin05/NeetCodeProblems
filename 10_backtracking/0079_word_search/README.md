# 79. Word Search

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/word-search/

## Task

You get an `m x n` grid of letters `board` and a string `word`. Return `true` if `word` can be
found in the grid, `false` otherwise.

The word is read along a path of cells where each next cell is a horizontal or vertical
neighbour of the previous one (not diagonal). A cell may be used at most once in the same word.

## Examples

**Example 1**

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

**Example 2**

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

**Example 3**

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

The board in all three examples:

```
A B C E
S F C S
A D E E
```

## Constraints

- `m == board.length`
- `n = board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consists of only lowercase and uppercase English letters.

## Follow-up

Could you use search pruning to make your solution faster with a larger `board`?

## Hints

<details><summary>Hint 1</summary>

The path can start at any cell. Once it has started, from each cell there are at most four ways to continue.

</details>

<details><summary>Hint 2</summary>

A path can go a long way and then get stuck. When that happens, what has to be undone so that other paths can still use those cells?

</details>

<details><summary>Hint 3</summary>

For the follow-up: some words can be ruled out before any path is tried at all. What could you check about the letters of the board first?

</details>
