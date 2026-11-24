# 680. Valid Palindrome II

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/valid-palindrome-ii/

## Task

You get a string `s` of lowercase English letters. You may delete at most one character from it.
Return `true` if `s` can read the same forwards and backwards after that, `false` otherwise.

Deleting nothing is allowed, so a string that is already a palindrome gives `true`.

## Examples

**Example 1**

```
Input: s = "aba"
Output: true
```

**Example 2**

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

**Example 3**

```
Input: s = "abc"
Output: false
```

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of lowercase English letters.

## Hints

<details><summary>Hint 1</summary>

Trying every position to delete and checking each result is O(n^2): about `10^10` steps for the
longest strings. Where can the one deletion actually help?

</details>

<details><summary>Hint 2</summary>

Compare characters from both ends towards the middle. As long as they match, nothing needs to be
deleted. What choices do you have at the first pair that does not match?

</details>

<details><summary>Hint 3</summary>

At that first mismatch, picking one side by looking only at the next characters can go wrong.
Try `"cbbcc"` and `"ccbbc"` by hand.

</details>
