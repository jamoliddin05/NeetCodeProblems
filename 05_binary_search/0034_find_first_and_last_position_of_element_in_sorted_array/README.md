# 34. Find First and Last Position of Element in Sorted Array

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## Task

You get an array of integers `nums` sorted in non-decreasing order (values can repeat) and an
integer `target`. Return `[first, last]`: the index of the first and of the last occurrence of
`target` in `nums`. If `target` is not in `nums`, return `[-1, -1]`.

Your algorithm must run in O(log n) time.

## Examples

**Example 1**

```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

**Example 2**

```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

**Example 3**

```
Input: nums = [], target = 0
Output: [-1,-1]
```

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array.
- `-10^9 <= target <= 10^9`

## Target complexity

O(log n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

Finding some index that holds `target` is not enough: in `[8, 8, 8, 8]` it could be any of them.
After you find a match, what do you still not know?

</details>

<details><summary>Hint 2</summary>

The first and the last position can be found by two searches that differ in one small detail:
what to do when the middle element equals `target`.

</details>

<details><summary>Hint 3</summary>

Walking left and right from a match one step at a time is O(n) when the whole array equals
`target`.

</details>
