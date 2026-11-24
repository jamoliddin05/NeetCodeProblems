# 242. Valid Anagram

**Easy** · Hash Table, String, Sorting ·
[NeetCode](https://neetcode.io/problems/is-anagram/question?list=neetcode150) ·
[LeetCode](https://leetcode.com/problems/valid-anagram/)

You get two strings `s` and `t`. Return `true` if `t` is a rearrangement of `s`, meaning both
contain exactly the same letters, each the same number of times. Otherwise return `false`.

**Example 1**

```text
Input: s = "racecar", t = "carrace"
Output: true
```

**Example 2**

```text
Input: s = "jar", t = "jam"
Output: false
```

**Constraints**

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

<details><summary>Target complexity</summary>

`O(n + m)` time and `O(1)` space, where `n` is the length of `s` and `m` is the length of `t`.

</details>

<details><summary>Hint 1</summary>

The order of the letters doesn't matter, only how many times each one appears.

</details>

<details><summary>Hint 2</summary>

There are only 26 possible letters. How much memory does that really take?

</details>

<details><summary>Hint 3</summary>

Comparing only *which* letters appear isn't enough: `"aab"` and `"abb"` use the same letters.

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
