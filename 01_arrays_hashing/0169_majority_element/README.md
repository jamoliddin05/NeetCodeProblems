# 169. Majority Element

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/majority-element/

## Task

You get an array `nums` of length `n`. One value in it appears more than `⌊n / 2⌋` times, which
means it fills more than half of the array. Return that value.

The input always contains such a value.

## Examples

**Example 1**

```
Input: nums = [3,2,3]
Output: 3
```

**Example 2**

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

## Constraints

- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`
- The input is generated such that a majority element exists in the array.

## Target complexity

Follow-up from the site: O(n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

Counting every value with a dictionary works in O(n) time. The follow-up asks you to drop the
dictionary. What do you lose, and do you really need it?

</details>

<details><summary>Hint 2</summary>

Suppose you remove two different values from the array at the same time. Is the majority value
still the majority of what is left?

</details>

<details><summary>Hint 3</summary>

Take Example 2 on paper and keep crossing out two different values at a time. What is left at
the end?

</details>
