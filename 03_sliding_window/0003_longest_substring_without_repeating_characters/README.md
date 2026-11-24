# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Task

You get a string `s`. Find the longest substring of `s` in which no character appears twice,
and return its length.

A substring is a block of characters that stand next to each other in `s`. Picking characters
from different places, with gaps between them, gives a subsequence, and that does not count.

## Examples

**Example 1**

```
Input: s = "abcabcbb"
Output: 3
```

The answer is "abc", with the length of 3. "bca" and "cab" are also correct answers.

**Example 2**

```
Input: s = "bbbbb"
Output: 1
```

The answer is "b", with the length of 1.

**Example 3**

```
Input: s = "pwwkew"
Output: 3
```

The answer is "wke", with the length of 3.
"pwke" is a subsequence, not a substring, so it does not count.

## Constraints

- `0 <= s.length <= 10^5`
- `s` consists of English letters, digits, symbols and spaces.

## Target complexity

O(n) time, where n is the length of `s`, and O(m) space, where m is the number of different characters.

## Hints

<details><summary>Hint 1</summary>

Checking every substring is O(n^2) substrings, each with its own check. Suppose the block from `i` to `j` has no repeats. When you add the character at `j + 1`, what do you know already?

</details>

<details><summary>Hint 2</summary>

If the new character is already inside the block, the block has to lose some characters from its left side. Which ones, at the least?

</details>

<details><summary>Hint 3</summary>

Try your idea on `"abba"` and on `"dvdf"` by hand.

</details>
