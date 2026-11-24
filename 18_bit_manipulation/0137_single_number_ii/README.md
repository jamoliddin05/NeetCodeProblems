# 137. Single Number II

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/single-number-ii/

## Task

You get an integer array `nums`. Every value in it appears exactly three times, except one value
that appears only once. Return that value.

Your solution must run in linear time and use only constant extra space.

## Examples

**Example 1**

```
Input: nums = [2,2,3,2]
Output: 3
```

**Example 2**

```
Input: nums = [0,1,0,1,0,1,99]
Output: 99
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Every element appears exactly three times, except for one element that appears once.

## Target complexity

O(n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

The idea from Single Number doesn't work here: three copies of a value don't combine to `0`. Look
at the numbers one bit position at a time instead.

</details>

<details><summary>Hint 2</summary>

At one bit position, count how many numbers have a 1 there. What does that count tell you about the
same bit of the single value?

</details>

<details><summary>Hint 3</summary>

Values can be negative, and a Python int has no fixed size. If you build the answer bit by bit,
check what you do with bit 31, the sign bit of a 32-bit integer.

</details>
