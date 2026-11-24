# 36. Valid Sudoku

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/valid-sudoku/

## Task

You get a `9 x 9` Sudoku board that is partly filled. Each cell holds a digit `"1"` to `"9"` or
`"."` for an empty cell. Return `true` if the filled cells break none of these rules, `false`
otherwise:

1. No digit appears twice in the same row.
2. No digit appears twice in the same column.
3. No digit appears twice in the same `3 x 3` box. The board is split into nine such boxes.

Check only the cells that are filled. A board can pass these rules and still have no solution;
that still counts as valid.

## Examples

**Example 1**

```
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
```

**Example 2**

```
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
```

Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are
two 8's in the top left 3x3 sub-box, it is invalid.

## Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `1-9` or `'.'`.

## Hints

<details><summary>Hint 1</summary>

Every filled cell belongs to exactly one row, one column and one box. What do you need to
remember about each of them to spot a repeat?

</details>

<details><summary>Hint 2</summary>

Rows and columns are numbered by `r` and `c` already. How can you number the nine boxes from the
same `r` and `c`?

</details>

<details><summary>Hint 3</summary>

Check your box numbering on cells `(0, 3)` and `(3, 0)`: they are in different boxes.

</details>
