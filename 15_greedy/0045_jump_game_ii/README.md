# 45. Jump Game II

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/jump-game-ii/

## Task

You get an integer array `nums` of length `n` and start on index `0`. The value `nums[i]` is the
longest forward jump from index `i`: from there you can move to any index `i + j` where
`0 <= j <= nums[i]` and `i + j < n`.

Return the smallest number of jumps you need to reach index `n - 1`. The tests always make it
possible to reach it.

## Examples

**Example 1**

```
Input: nums = [2,3,1,1,4]
Output: 2
```

Jump 1 step from index 0 to index 1, then 3 steps to the last index.

**Example 2**

```
Input: nums = [2,3,0,1,4]
Output: 2
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`
- It's guaranteed that you can reach `nums[n - 1]`.

## Target complexity

O(n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

Jumping as far as possible every time is not always best: in Example 1 the longest first jump
lands on index 2, and from there you need two more jumps.

</details>

<details><summary>Hint 2</summary>

Which indexes can you reach with exactly one jump? Which ones need exactly two? What shape do
these groups of indexes have?

</details>
