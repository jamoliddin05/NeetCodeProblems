# 1143. Longest Common Subsequence

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/longest-common-subsequence/

## Task

You get two strings `text1` and `text2`. A subsequence of a string is what is left after deleting
some of its characters (or none) without changing the order of the rest. For example, `"ace"` is a
subsequence of `"abcde"`.

Return the length of the longest string that is a subsequence of both `text1` and `text2`. If they
have no common subsequence, return `0`.

## Examples

**Example 1**

```
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
```

**Example 2**

```
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

**Example 3**

```
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

## Constraints

- `1 <= text1.length, text2.length <= 1000`
- `text1` and `text2` consist of only lowercase English characters.

## Hints

<details><summary>Hint 1</summary>

Compare the first characters of the two strings. If they are equal, can pairing them with each other ever make the answer worse?

</details>

<details><summary>Hint 2</summary>

If they are different, at least one of the two first characters is not part of the answer. Which smaller questions does that leave?

</details>

<details><summary>Hint 3</summary>

Every such smaller question is fixed by two positions, one in each string. How many different pairs of positions are there?

</details>
