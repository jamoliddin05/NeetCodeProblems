# 1. Two Sum

**Easy** · Array, Hash Table ·
[NeetCode](https://neetcode.io/problems/two-integer-sum/question?list=neetcode150) ·
[LeetCode](https://leetcode.com/problems/two-sum/)

You get an integer array `nums` and an integer `target`. Find two **different** positions `i`
and `j` whose values add up to `target`, and return `[i, j]` with the smaller index first.
The two positions may hold equal values, but you can't use one position twice. Every input
has exactly one such pair.

**Example 1**

```text
Input: nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
```

**Example 2**

```text
Input: nums = [4,5,6], target = 10
Output: [0,2]
```

**Example 3**

```text
Input: nums = [5,5], target = 10
Output: [0,1]
```

**Constraints**

- `2 <= nums.length <= 1000`
- `-10,000,000 <= nums[i] <= 10,000,000`
- `-10,000,000 <= target <= 10,000,000`
- Only one valid answer exists.

<details><summary>Target complexity</summary>

`O(n)` time and `O(n)` space, where `n` is the length of `nums`.

</details>

<details><summary>Hint 1</summary>

Checking every pair works and is `O(n^2)`. Can you do it in a single pass?

</details>

<details><summary>Hint 2</summary>

For a value `x`, you already know exactly which other value it needs. What lets you ask
"have I seen that value, and where?" in constant time?

</details>

<details><summary>Hint 3</summary>

`[3, 2, 4]` with `target = 6` must give `[1, 2]`, not `[0, 0]`.

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
