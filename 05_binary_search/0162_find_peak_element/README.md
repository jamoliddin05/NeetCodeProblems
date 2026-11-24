# 162. Find Peak Element

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/find-peak-element/

## Task

A peak is an element that is strictly greater than each of its neighbors.

You get an integer array `nums` in which no two neighbors are equal. Return the index of any
peak. If there are several peaks, any one of them is a correct answer.

Treat the positions outside the array as minus infinity: `nums[-1] = nums[n] = -∞`. So the first
and the last element only need to be greater than their one neighbor inside the array.

Your algorithm must run in O(log n) time.

## Examples

**Example 1**

```
Input: nums = [1,2,3,1]
Output: 2
```

3 is a peak, and its index is 2.

**Example 2**

```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
```

Index 1 (value 2) and index 5 (value 6) are both peaks, so either answer is accepted.

## Constraints

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`

## Target complexity

O(log n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

Because of the -∞ outside both ends, a peak always exists. You don't need to find all peaks, so
you don't need to look at the whole array.

</details>

<details><summary>Hint 2</summary>

Suppose `nums[i] < nums[i + 1]`. Start at `i + 1` and keep walking right while the values go up.
Can you walk forever without reaching a peak?

</details>

<details><summary>Hint 3</summary>

Watch out for code that uses `-2^31` in place of -∞: the array itself can contain that value.

</details>
