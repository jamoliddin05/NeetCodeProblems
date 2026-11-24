# 16. 3Sum Closest

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/3sum-closest/

## Task

You get an integer array `nums` and an integer `target`. Pick three numbers from `nums` at three
different positions so that their sum is as close to `target` as possible. Return that sum (the
sum itself, not its distance from `target`).

Each input has exactly one closest sum.

## Examples

**Example 1**

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```

**Example 2**

```
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
```

## Constraints

- `3 <= nums.length <= 500`
- `-1000 <= nums[i] <= 1000`
- `-10^4 <= target <= 10^4`

## Hints

<details><summary>Hint 1</summary>

Trying every set of three is O(n^3): about 20 million sets at `n = 500`, too slow in Python.
Fix one of the three numbers. What is left to solve for the other two?

</details>

<details><summary>Hint 2</summary>

Finding two numbers with a sum near some value is much easier when the numbers are in a known
order.

</details>

<details><summary>Hint 3</summary>

Each time you look at a candidate sum, you learn whether it is too small or too large. Which
change makes it larger, and which makes it smaller?

</details>
