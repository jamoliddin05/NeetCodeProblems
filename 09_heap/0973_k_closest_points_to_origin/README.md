# 973. K Closest Points to Origin

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/k-closest-points-to-origin/

## Task

You get an array `points`, where `points[i] = [x_i, y_i]` is a point on the X-Y plane, and an
integer `k`. Return the `k` points that are closest to the origin `(0, 0)`.

Distance is the usual straight-line (Euclidean) distance: `sqrt((x1 - x2)^2 + (y1 - y2)^2)`.

The points may be returned in any order. The test data guarantees that the set of `k` closest
points is unique.

## Examples

**Example 1**

```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
```

The distance between (1, 3) and the origin is sqrt(10). The distance between (-2, 2) and the
origin is sqrt(8). Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin. We only want the
closest k = 1 points, so the answer is just [[-2,2]].

**Example 2**

```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

The answer [[-2,4],[3,3]] would also be accepted.

## Constraints

- `1 <= k <= points.length <= 10^4`
- `-10^4 <= x_i, y_i <= 10^4`

## Hints

<details><summary>Hint 1</summary>

To compare two points by distance, do you need the square root at all?

</details>

<details><summary>Hint 2</summary>

The answer is only the `k` closest points, in any order. How much of the full order of all points do you really need?

</details>

<details><summary>Hint 3</summary>

While scanning the points, which point in your current group of candidates is the first one to be replaced by a closer point?

</details>
