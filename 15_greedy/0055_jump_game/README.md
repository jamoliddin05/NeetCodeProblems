# 55. Jump Game

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/jump-game/

## Task

You get an integer array `nums` and start on index `0`. The value `nums[i]` is the longest jump
you can make from index `i`: from there you can move forward by any number of steps from `0` up
to `nums[i]`.

Return `true` if you can reach the last index, `false` otherwise.

## Examples

**Example 1**

```
Input: nums = [2,3,1,1,4]
Output: true
```

Jump 1 step from index 0 to index 1, then 3 steps to the last index.

**Example 2**

```
Input: nums = [3,2,1,0,4]
Output: false
```

Every path ends on index 3. Its jump length is 0, so you can't move from there to the last index.

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

## Target complexity

O(n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

The only way to get stuck is to land on an index you can't leave. Which value makes that happen,
and when can you jump past it?

</details>

<details><summary>Hint 2</summary>

Checking from every index which later indexes it reaches is O(n^2). Go from left to right
instead: what single number about the indexes you have already passed tells you whether you can
stand on the next one?

</details>
