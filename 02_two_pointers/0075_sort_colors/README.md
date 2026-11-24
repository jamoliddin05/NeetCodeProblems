# 75. Sort Colors

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/sort-colors/

## Task

You get an array `nums` where every value is `0` (red), `1` (white) or `2` (blue). Rearrange it
in place so that all `0`s come first, then all `1`s, then all `2`s.

Don't use the library's sort function. The method returns nothing.

## Examples

**Example 1**

```
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all
1s, then all 2s.

**Example 2**

```
Input: nums = [2,0,1]
Output: [0,1,2]
```

The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.

## Constraints

- `n == nums.length`
- `1 <= n <= 300`
- `nums[i]` is either `0`, `1`, or `2`.

## Target complexity

Follow-up from the site: one pass over the array with O(1) extra space.

## Hints

<details><summary>Hint 1</summary>

There are only three possible values. A version that walks the array twice is simple; start
with it if the one-pass version seems hard.

</details>

<details><summary>Hint 2</summary>

For one pass: you know where the `0`s and the `2`s must end up. Can a value be sent to its final
area as soon as you see it?

</details>

<details><summary>Hint 3</summary>

If you swap in a value from a part of the array you have not reached yet, have you checked that
value?

</details>
