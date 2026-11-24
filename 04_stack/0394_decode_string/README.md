# 394. Decode String

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/decode-string/

## Task

You get an encoded string `s`. Return the decoded string.

The encoding rule is `k[text]`: the part inside the square brackets is repeated exactly `k`
times, where `k` is a positive integer. Groups can be nested, and letters can stand outside
any group.

You can rely on these facts about the input:

- It is always valid: no extra spaces, and the square brackets are correctly matched.
- The original text has no digits. Digits only appear as repeat counts `k`, so there are no
  inputs like `3a` or `2[4]`.
- The decoded string is never longer than `10^5` characters.

## Examples

**Example 1**

```
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
```

**Example 2**

```
Input: s = "3[a2[c]]"
Output: "accaccacc"
```

**Example 3**

```
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Constraints

- `1 <= s.length <= 30`
- `s` consists of lowercase English letters, digits, and square brackets `'[]'`.
- `s` is guaranteed to be a valid input.
- All the integers in `s` are in the range `[1, 300]`.

## Target complexity

O(n + m) time, where n is the length of `s` and m is the length of the decoded string.

## Hints

<details><summary>Hint 1</summary>

A count can have more than one digit, like `12[a]`.

</details>

<details><summary>Hint 2</summary>

When you reach `]`, you need two things that you saw earlier: the text inside this group and the count in front of it. When you reach `[`, what must you put aside so you can come back to it later?

</details>

<details><summary>Hint 3</summary>

Work through `"3[a2[c]]"` by hand, writing down what you have built so far at each character.

</details>
