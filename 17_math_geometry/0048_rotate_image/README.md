# 48. Rotate Image

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/rotate-image/

## Task

You get an `n x n` matrix that stands for an image. Turn it 90 degrees clockwise.

Do it in place: change `matrix` itself and don't create a second 2D matrix. The method returns
nothing; the tests look at `matrix` after the call.

## Examples

**Example 1**

```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

**Example 2**

```
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Hints

<details><summary>Hint 1</summary>

Where does `matrix[i][j]` end up after the turn? Write its new row and column using `i`, `j` and `n`.

</details>

<details><summary>Hint 2</summary>

When you move one value to its new place, you overwrite the value that was there. Where must that
one go? Follow the chain until it comes back to where it started.

</details>

<details><summary>Hint 3</summary>

A clockwise turn can also be made from two simpler changes of the matrix, each of which is easy to
do in place.

</details>
