# 435. Non-overlapping Intervals

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/non-overlapping-intervals/

## Task

You get an array `intervals` where `intervals[i] = [start_i, end_i]`. Return the smallest number
of intervals you have to remove so that no two of the remaining intervals overlap.

Here intervals that only touch at one point do **not** overlap: `[1,2]` and `[2,3]` can both stay.

## Examples

**Example 1**

```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
```

Remove `[1,3]`; the other three only touch each other.

**Example 2**

```
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
```

Two of the three copies of `[1,2]` have to go.

**Example 3**

```
Input: intervals = [[1,2],[2,3]]
Output: 0
```

The two intervals only touch, so nothing has to be removed.

## Constraints

- `1 <= intervals.length <= 10^5`
- `intervals[i].length == 2`
- `-5 * 10^4 <= start_i < end_i <= 5 * 10^4`

## Target complexity

O(n log n) time, where n is the length of `intervals`.

## Hints

<details><summary>Hint 1</summary>

Removing as few intervals as possible is the same as keeping as many as possible.

</details>

<details><summary>Hint 2</summary>

Of two overlapping intervals, which one leaves more room for the intervals that come after it?

</details>
