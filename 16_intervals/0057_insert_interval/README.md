# 57. Insert Interval

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/insert-interval/

## Task

You get `intervals`, a list of intervals `[start_i, end_i]` that don't overlap each other and are
sorted by `start_i` in ascending order. You also get one more interval,
`newInterval = [start, end]`.

Add `newInterval` to the list so that the list is still sorted by start and still has no
overlapping intervals: merge `newInterval` with every interval it overlaps. Two intervals overlap
if they share at least one point, so `[1,2]` and `[2,3]` overlap.

Return the resulting list. You don't have to change `intervals` in place; you can build a new
list and return it.

## Examples

**Example 1**

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2**

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
```

`[4,8]` overlaps `[3,5]`, `[6,7]` and `[8,10]`, so all four merge into `[3,10]`.

## Constraints

- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in ascending order.
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

## Target complexity

O(n) time, where n is the length of `intervals`.

## Hints

<details><summary>Hint 1</summary>

Some intervals in the list can't touch `newInterval` at all. Where in the list are they?

</details>

<details><summary>Hint 2</summary>

When `newInterval` overlaps several intervals, what are the start and the end of the merged
interval?

</details>

<details><summary>Hint 3</summary>

`intervals` can be empty, and `newInterval` can belong before the first interval or after the
last one.

</details>
