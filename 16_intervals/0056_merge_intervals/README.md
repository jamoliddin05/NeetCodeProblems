# 56. Merge Intervals

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/merge-intervals/

## Task

You get an array `intervals` where `intervals[i] = [start_i, end_i]`. Merge every group of
intervals that overlap, and return the intervals that are left: they must not overlap each other
and must cover exactly the same points as the input.

Intervals that only share an endpoint, like `[1,4]` and `[4,5]`, count as overlapping. The input
is not sorted. You may return the merged intervals in any order.

## Examples

**Example 1**

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

`[1,3]` and `[2,6]` overlap, so they merge into `[1,6]`.

**Example 2**

```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
```

`[1,4]` and `[4,5]` share the point 4, so they overlap.

**Example 3**

```
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
```

`[1,4]` and `[4,7]` overlap, even though they come in the other order.

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Target complexity

O(n log n) time and O(n) space, where n is the length of `intervals`.

## Hints

<details><summary>Hint 1</summary>

Comparing every pair of intervals is O(n^2). If the intervals came in a useful order, which ones
could a given interval overlap?

</details>

<details><summary>Hint 2</summary>

When two intervals merge, the end of the result is not always the end of the one that starts
later: think of `[1,10]` and `[2,3]`.

</details>
