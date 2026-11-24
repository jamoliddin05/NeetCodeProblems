# 215. Kth Largest Element in an Array

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/kth-largest-element-in-an-array/

## Task

You get an integer array `nums` and an integer `k`. Return the `k`-th largest element of the
array.

This is the `k`-th element when the array is sorted from largest to smallest, so equal values
are counted separately: it is not the `k`-th largest distinct value.

## Examples

**Example 1**

```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

**Example 2**

```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

## Constraints

- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Follow-up

Can you solve it without sorting the array?

## Hints

<details><summary>Hint 1</summary>

To answer, you do not need the full order of the array. Which elements actually matter for the `k`-th largest?

</details>

<details><summary>Hint 2</summary>

If you scan the array once, what is the smallest set of values you have to remember along the way?

</details>

<details><summary>Hint 3</summary>

Many equal values in a row, or an array that is already sorted, are where some fast-on-average methods slow down a lot. The last cases in `inputs.txt` check this.

</details>
