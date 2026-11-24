# 125. Valid Palindrome

**Easy** · Two Pointers, String ·
[NeetCode](https://neetcode.io/problems/is-palindrome/question?list=neetcode150) ·
[LeetCode](https://leetcode.com/problems/valid-palindrome/)

You get a string `s`. Return `true` if it reads the same forwards and backwards once you keep only
letters and digits and treat upper- and lowercase letters as equal. Otherwise return `false`.

**Example 1**

```text
Input: s = "Was it a car or a cat I saw?"
Output: true
```

After filtering, the string is `"wasitacaroracatisaw"`, which is a palindrome.

**Example 2**

```text
Input: s = "tab a cat"
Output: false
```

After filtering, the string is `"tabacat"`, which is not a palindrome.

**Constraints**

- `1 <= s.length <= 1000`
- `s` is made up of only printable ASCII characters.

<details><summary>Target complexity</summary>

`O(n)` time and `O(1)` extra space, where `n` is the length of `s`.

</details>

<details><summary>Hint 1</summary>

Building a cleaned-up copy works, but it costs `O(n)` memory. Can you check without making one?

</details>

<details><summary>Hint 2</summary>

Digits are alphanumeric too, and `"0"` is not the same character as `"O"`.

</details>

<details><summary>Hint 3</summary>

What should happen when the string contains no letters or digits at all?

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
