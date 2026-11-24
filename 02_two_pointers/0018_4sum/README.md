# 18. 4Sum

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/4sum/

## Task

You get an integer array `nums` and an integer `target`. Return every group of four numbers
`[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- `a`, `b`, `c` and `d` are four different positions.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

The same group of values must not appear twice in the answer. The groups can come in any order,
and so can the numbers inside each group.

## Examples

**Example 1**

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

**Example 2**

```
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
```

## Constraints

- `1 <= nums.length <= 200`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`

## Hints

<details><summary>Hint 1</summary>

Trying every group of four is O(n^4): about 65 million groups at `n = 200`, too slow in Python.
How did you handle the same task for three numbers? Can the same idea take one more number?

</details>

<details><summary>Hint 2</summary>

Repeated values are the hard part. If the values are in a known order, where do equal values
sit, and how can you avoid starting from the same value twice?

</details>

<details><summary>Hint 3</summary>

Shortcuts that stop a loop early must still be correct when `target` and the numbers are
negative.

</details>
