# 560. Subarray Sum Equals K

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/subarray-sum-equals-k/

## Task

You get an integer array `nums` and an integer `k`. Count how many subarrays of `nums` add up to
exactly `k`, and return that count.

A subarray is a run of one or more elements that sit next to each other in the array. Two
subarrays at different positions are counted separately, even if they hold the same values.

## Examples

**Example 1**

```
Input: nums = [1,1,1], k = 2
Output: 2
```

**Example 2**

```
Input: nums = [1,2,3], k = 3
Output: 2
```

## Constraints

- `1 <= nums.length <= 2 * 10^4`
- `-1000 <= nums[i] <= 1000`
- `-10^7 <= k <= 10^7`

## Hints

<details><summary>Hint 1</summary>

Checking every pair of start and end is O(n^2): about 200 million pairs at `n = 2 * 10^4`, too
slow here. Note that `nums` can hold negative numbers. Which common array technique does that
rule out?

</details>

<details><summary>Hint 2</summary>

The sum of the elements from index `i` to index `j` can be written using two sums that both
start at index 0.

</details>

<details><summary>Hint 3</summary>

While you walk from left to right, what would you need to remember about the part you already
passed to answer "how many subarrays ending here sum to `k`?" in one step?

</details>
