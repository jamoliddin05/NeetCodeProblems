# 452. Minimum Number of Arrows to Burst Balloons

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

## Task

Balloons are taped to a flat wall. Balloon `i` stretches across the x-coordinates from
`points[i][0]` to `points[i][1]`; you don't know where it is vertically.

You can shoot arrows straight up from any point `x` on the x-axis. An arrow shot from `x` bursts
every balloon with `x_start <= x <= x_end` (both ends included) and keeps flying after it hits a
balloon. You can shoot as many arrows as you like.

Return the smallest number of arrows that bursts all the balloons.

## Examples

**Example 1**

```
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
```

An arrow at x = 6 bursts `[2,8]` and `[1,6]`. An arrow at x = 11 bursts `[10,16]` and `[7,12]`.

**Example 2**

```
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
```

No two balloons share a point, so each one needs its own arrow.

**Example 3**

```
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
```

An arrow at x = 2 bursts `[1,2]` and `[2,3]`. An arrow at x = 4 bursts `[3,4]` and `[4,5]`.

## Constraints

- `1 <= points.length <= 10^5`
- `points[i].length == 2`
- `-2^31 <= x_start < x_end <= 2^31 - 1`

## Target complexity

O(n log n) time, where n is the length of `points`.

## Hints

<details><summary>Hint 1</summary>

Balloons that only touch at one point can be burst by one arrow (Example 3).

</details>

<details><summary>Hint 2</summary>

Moving an arrow along the x-axis costs nothing as long as it still hits the same balloons. How
far can you move each arrow without losing any of its balloons?

</details>

<details><summary>Hint 3</summary>

Coordinates go down to `-2^31`. If you start from a placeholder value, make sure no real balloon
can match it.

</details>
