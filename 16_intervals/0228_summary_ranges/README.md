# 228. Summary Ranges

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/summary-ranges/

## Task

You get an array `nums` of distinct integers sorted in ascending order. A range `[a,b]` means
every integer from `a` to `b`, both included.

Describe `nums` with the shortest sorted list of ranges such that every number in `nums` is in
exactly one range, and every integer in a range is in `nums`.

Return the ranges as strings:

- `"a->b"` if `a != b`
- `"a"` if `a == b`

## Examples

**Example 1**

```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
```

The ranges are `[0,2]`, `[4,5]` and `[7,7]`.

**Example 2**

```
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
```

The ranges are `[0,0]`, `[2,4]`, `[6,6]` and `[8,9]`.

## Constraints

- `0 <= nums.length <= 20`
- `-2^31 <= nums[i] <= 2^31 - 1`
- All the values of `nums` are unique.
- `nums` is sorted in ascending order.

## Target complexity

O(n) time, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

When do two numbers that stand next to each other in `nums` belong to the same range?

</details>

<details><summary>Hint 2</summary>

`nums` can be empty, and the last range must be added to the answer too.

</details>
