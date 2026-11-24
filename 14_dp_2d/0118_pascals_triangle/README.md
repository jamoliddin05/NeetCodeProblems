# 118. Pascal's Triangle

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/pascals-triangle/

## Task

You get an integer `numRows`. Return the first `numRows` rows of Pascal's triangle, as a list of
rows.

The first row is `[1]`. Each next row is one number longer than the row above it: it starts and
ends with `1`, and every number between them is the sum of the two numbers directly above it.

```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

## Examples

**Example 1**

```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

**Example 2**

```
Input: numRows = 1
Output: [[1]]
```

## Constraints

- `1 <= numRows <= 30`

## Hints

<details><summary>Hint 1</summary>

Write rows 1 to 5 by hand. Which two numbers of the row above give the number at position `j` of the current row?

</details>

<details><summary>Hint 2</summary>

To build a row, which rows of the triangle do you need to look at?

</details>
