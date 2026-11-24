# 136. Single Number

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/single-number/

## Task

You get a non-empty integer array `nums`. Every value in it appears exactly twice, except one value
that appears only once. Return that value.

Your solution must run in linear time and use only constant extra space.

## Examples

**Example 1**

```
Input: nums = [2,2,1]
Output: 1
```

**Example 2**

```
Input: nums = [4,1,2,1,2]
Output: 4
```

**Example 3**

```
Input: nums = [1]
Output: 1
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`
- Every element appears twice, except for one element that appears only once.

## Target complexity

O(n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

A set or a counter gives O(n) time, but not O(1) space. You need to combine all the numbers into
one value while you read them.

</details>

<details><summary>Hint 2</summary>

Look at the bitwise operators. Is there one where a number combined with itself gives `0`, and a
number combined with `0` stays the same?

</details>
