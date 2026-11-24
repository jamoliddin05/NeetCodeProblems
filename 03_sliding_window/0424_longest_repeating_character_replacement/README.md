# 424. Longest Repeating Character Replacement

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/longest-repeating-character-replacement/

## Task

You get a string `s` of uppercase English letters and an integer `k`.
You may change any character of `s` into any other uppercase letter, at most `k` times in total.

Return the length of the longest substring made of one repeated letter that you can get this way.

## Examples

**Example 1**

```
Input: s = "ABAB", k = 2
Output: 4
```

Replace the two 'A's with two 'B's, or the other way round.

**Example 2**

```
Input: s = "AABABBA", k = 1
Output: 4
```

Replace the one 'A' in the middle with 'B' and get "AABBBBA".
The substring "BBBB" has the longest run of one letter, which is 4.
Other choices of replacement may give this answer too.

## Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

## Target complexity

O(n) time and O(1) extra space (the alphabet has only 26 letters), where n is the length of `s`.

## Hints

<details><summary>Hint 1</summary>

Look at one substring. How many replacements does it need to become one repeated letter? Which letter is the best one to keep?

</details>

<details><summary>Hint 2</summary>

A substring is good when the number from Hint 1 is at most `k`. Checking every substring is O(n^2). If a substring is good, is every shorter substring inside it good too?

</details>

<details><summary>Hint 3</summary>

Try `s = "AAABBBAAA"` with `k = 2` and with `k = 3` by hand.

</details>
