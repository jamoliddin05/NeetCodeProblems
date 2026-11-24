# 153. Find Minimum in Rotated Sorted Array

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Task

An array of `n` distinct integers was sorted in ascending order and then rotated between 1 and
`n` times. One rotation moves the last element to the front: `[a0, a1, ..., a(n-1)]` becomes
`[a(n-1), a0, a1, ..., a(n-2)]`. For example, `[0,1,2,4,5,6,7]` becomes `[4,5,6,7,0,1,2]` after
4 rotations, and stays `[0,1,2,4,5,6,7]` after 7 rotations.

You get the rotated array `nums`. Return its smallest element.

Your algorithm must run in O(log n) time.

## Examples

**Example 1**

```
Input: nums = [3,4,5,1,2]
Output: 1
```

The original array was `[1,2,3,4,5]`, rotated 3 times.

**Example 2**

```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
```

The original array was `[0,1,2,4,5,6,7]`, rotated 4 times.

**Example 3**

```
Input: nums = [11,13,15,17]
Output: 11
```

The original array was `[11,13,15,17]`, rotated 4 times, so it looks unchanged.

## Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are unique.
- `nums` is sorted and rotated between `1` and `n` times.

## Target complexity

O(log n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

A rotated array is two sorted runs placed one after the other, and every value in the first run
is larger than every value in the second run. The smallest element is where the second run
starts.

</details>

<details><summary>Hint 2</summary>

Given any one index, can you tell with a single comparison which of the two runs it belongs to?

</details>

<details><summary>Hint 3</summary>

An array rotated `n` times is not rotated at all, so there is only one run. Make sure your code
handles that.

</details>
