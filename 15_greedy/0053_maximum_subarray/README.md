# 53. Maximum Subarray

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/maximum-subarray/

## Task

You get an integer array `nums`. A subarray is a non-empty run of elements that stand next to
each other in `nums`. Find the subarray whose elements add up to the largest sum and return that
sum.

## Examples

**Example 1**

```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
```

The subarray `[4,-1,2,1]` has the largest sum, 6.

**Example 2**

```
Input: nums = [1]
Output: 1
```

**Example 3**

```
Input: nums = [5,4,-1,7,8]
Output: 23
```

The whole array is the best subarray here.

## Constraints

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Target complexity

O(n) time and O(1) extra space, where n is the length of `nums`.

**Follow-up:** once you have the O(n) solution, try writing another one that uses divide and
conquer.

## Hints

<details><summary>Hint 1</summary>

The subarray can't be empty, so the answer can be negative. What should `[-3, -1, -2]` return?

</details>

<details><summary>Hint 2</summary>

Trying every start and every end is O(n^2): about 5 * 10^9 steps for n = 10^5. Which work in
that approach gets repeated?

</details>

<details><summary>Hint 3</summary>

Look only at the subarrays that end exactly at index `i`. How is the best of them related to the
best of the subarrays that end exactly at index `i - 1`?

</details>
