# 1584. Min Cost to Connect All Points

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/min-cost-to-connect-all-points/

## Task

You get a list `points` of points with integer coordinates on a plane, where
`points[i] = [x, y]`.

Connecting two points `[xi, yi]` and `[xj, yj]` costs their Manhattan distance:
`|xi - xj| + |yi - yj|`.

Return the lowest total cost of connections that link all the points together, so that between
any two points there is exactly one path along the chosen connections.

## Examples

**Example 1**

```
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
```

One way to reach 20: connect `[0,0]-[2,2]` (4), `[2,2]-[5,2]` (3), `[5,2]-[7,0]` (4) and
`[2,2]-[3,10]` (9). Between every pair of points there is exactly one path.

**Example 2**

```
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
```

## Constraints

- `1 <= points.length <= 1000`
- `-10^6 <= xi, yi <= 10^6`
- All pairs `(xi, yi)` are distinct.

## Target complexity

O(n^2 log n) time and O(n^2) space, where n is the number of points.

## Hints

<details><summary>Hint 1</summary>

Any two points can be connected. Think of every pair of points as a possible connection with its
own cost. How many connections does the answer use in total?

</details>

<details><summary>Hint 2</summary>

Linking each point to its nearest neighbour is not enough: the points can end up in separate
groups that are not linked to each other.

</details>

<details><summary>Hint 3</summary>

Grow one connected group step by step. At each step, which single new connection is always safe
to add?

</details>
