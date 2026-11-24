# 5. Longest Palindromic Substring

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/longest-palindromic-substring/

## Task

You get a string `s`. Return its longest palindromic substring: a run of consecutive characters
of `s` that reads the same from left to right and from right to left.

If several substrings share the longest length, any one of them is accepted. Upper and lower case
letters are different characters.

## Examples

**Example 1**

```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

**Example 2**

```
Input: s = "cbbd"
Output: "bb"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters.

## Hints

<details><summary>Hint 1</summary>

If `"aba"` is a palindrome, is `"xabax"` one too? What about `"xabay"`?

</details>

<details><summary>Hint 2</summary>

Palindromes of even length, like `"abba"`, have no middle character. Make sure your idea covers both odd and even lengths.

</details>

<details><summary>Hint 3</summary>

Checking each of the O(n^2) substrings from scratch costs O(n) per check. Can a check reuse what you already know about a shorter substring?

</details>
