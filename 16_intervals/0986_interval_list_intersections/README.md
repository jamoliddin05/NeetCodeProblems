# 986. Interval List Intersections

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/interval-list-intersections/

## Task

You get two lists of closed intervals, `firstList` and `secondList`. Within each list the
intervals don't overlap each other and are sorted. Return the intersection of the two lists:
the sorted list of intervals made of the points that are covered by both lists.

A closed interval `[a, b]` with `a <= b` is the set of real numbers `x` with `a <= x <= b`. Two
closed intervals intersect in either nothing or another closed interval: `[1, 3]` and `[2, 4]`
intersect in `[2, 3]`, and `[1, 3]` and `[3, 5]` intersect in `[3, 3]`.

## Examples

**Example 1**

```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

**Example 2**

```
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
```

## Constraints

- `0 <= firstList.length, secondList.length <= 1000`
- `firstList.length + secondList.length >= 1`
- `0 <= start_i < end_i <= 10^9`
- `end_i < start_{i+1}`
- `0 <= start_j < end_j <= 10^9`
- `end_j < start_{j+1}`

## Target complexity

O(m + n) time, where m and n are the lengths of the two lists.

## Hints

<details><summary>Hint 1</summary>

For two intervals `[a, b]` and `[c, d]`, write down when they intersect and what the
intersection is, using only `max` and `min`.

</details>

<details><summary>Hint 2</summary>

Compare the first interval of each list. After you have handled their intersection, one of the
two can't intersect anything else in the other list. Which one?

</details>
