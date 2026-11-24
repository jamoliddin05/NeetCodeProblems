# 300. Longest Increasing Subsequence

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/longest-increasing-subsequence/

## Task

You get an integer array `nums`. A subsequence is what is left after deleting some elements (or
none) without changing the order of the rest.

Return the length of the longest subsequence that is strictly increasing: every element is larger
than the one before it. Equal values do not count as increasing.

## Examples

**Example 1**

```
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
```

**Example 2**

```
Input: nums = [0,1,0,3,2,3]
Output: 4
```

**Example 3**

```
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

## Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

## Follow-up

Can you solve it in `O(n log(n))` time?

## Hints

<details><summary>Hint 1</summary>

Starting at the first element and taking every larger element you meet does not work. Try `[3, 4, -1, 0, 1, 2]`.

</details>

<details><summary>Hint 2</summary>

For each position `i`, think about the longest increasing subsequence that ends exactly at `nums[i]`. Which earlier elements are allowed to come right before `nums[i]`?

</details>

<details><summary>Hint 3</summary>

For the follow-up: of all increasing subsequences of the same length found so far, which one is the most useful to keep, and why?

</details>
