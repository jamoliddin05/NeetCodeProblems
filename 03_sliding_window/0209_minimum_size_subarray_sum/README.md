# 209. Minimum Size Subarray Sum

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/minimum-size-subarray-sum/

## Task

You get an array `nums` of positive integers and a positive integer `target`.
Find the shortest subarray (a block of elements next to each other) whose sum is at least
`target`, and return its length. If no subarray reaches `target`, return `0`.

## Examples

**Example 1**

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
```

The subarray [4,3] is the shortest one that reaches the target.

**Example 2**

```
Input: target = 4, nums = [1,4,4]
Output: 1
```

**Example 3**

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
```

## Constraints

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^4`

## Target complexity

O(n) time and O(1) extra space, where n is the length of `nums`.

Follow-up from LeetCode: once you have the O(n) solution, also write one that runs in O(n log n).

## Hints

<details><summary>Hint 1</summary>

All numbers are positive. What happens to the sum of a subarray when you make it longer on either side? When you make it shorter?

</details>

<details><summary>Hint 2</summary>

Suppose the subarray ending at index `j` and starting at index `i` is the shortest one that ends at `j` and reaches the target. For the subarrays ending at `j + 1`, can the best start be to the left of `i`?

</details>

<details><summary>Hint 3</summary>

For the O(n log n) follow-up: the running sums of a positive array only grow.

</details>
