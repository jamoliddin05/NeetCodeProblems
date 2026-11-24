# 733. Flood Fill

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/flood-fill/

## Task

You get an image as an `m x n` grid of integers `image`, where `image[i][j]` is the color of one
pixel, and three integers `sr`, `sc` and `color`.

Look at the color of the pixel `image[sr][sc]`; call it the start color. Paint that pixel with
`color`. Then paint every other pixel that has the start color and can be reached from the start
pixel by steps up, down, left or right (never diagonally) that only pass through pixels of the
start color.

Return the image after the painting.

## Examples

**Example 1**

```
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
```

The fill starts in the center. Every `1` connected to the center is painted `2`. The `1` in the
bottom-right corner touches the painted area only diagonally, so it keeps its color.

**Example 2**

```
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
```

The start pixel already has color `0`, so nothing changes.

## Constraints

- `m == image.length`
- `n == image[i].length`
- `1 <= m, n <= 50`
- `0 <= image[i][j], color < 2^16`
- `0 <= sr < m`
- `0 <= sc < n`

## Target complexity

O(m * n) time and O(m * n) space.

## Hints

<details><summary>Hint 1</summary>

Right after you paint a pixel, which pixels are the only new candidates for painting? Which of
them really need it?

</details>

<details><summary>Hint 2</summary>

Save the start color before you change anything. Once the start pixel is painted, you can no
longer read the start color from it.

</details>

<details><summary>Hint 3</summary>

What happens when `color` is equal to the start color? Make sure your solution still stops.

</details>
