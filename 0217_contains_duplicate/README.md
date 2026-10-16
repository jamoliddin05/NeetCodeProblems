# 217. Contains Duplicate

**Easy** · Array, Hash Table, Sorting ·
[NeetCode](https://neetcode.io/problems/duplicate-integer/question?list=neetcode150) ·
[LeetCode](https://leetcode.com/problems/contains-duplicate/)

You get an integer array `nums`. Return `true` if some value occurs at least twice in it, and
`false` if every value is distinct.

**Example 1**

```text
Input: nums = [1, 2, 3, 3]
Output: true
```

**Example 2**

```text
Input: nums = [1, 2, 3, 4]
Output: false
```

**Constraints**

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

<details><summary>Target complexity</summary>

`O(n)` time and `O(n)` space, where `n` is the length of `nums`.

</details>

<details><summary>Hint 1</summary>

Comparing every element with every other one works, but it's `O(n^2)` and will be too slow
at 10^5 elements.

</details>

<details><summary>Hint 2</summary>

While walking the array once, what would let you answer "have I seen this value already?"
in constant time?

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
