# 1249. Minimum Remove to Make Valid Parentheses

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

## Task

You get a string `s` made of `'('`, `')'` and lowercase English letters.
Remove as few parentheses as possible (`'('` or `')'`, from any positions) so that what is left
is a valid parentheses string, and return it. Letters are never removed.
If several strings are possible, return any one of them.

A parentheses string is valid when one of these holds:

- It is empty or contains only lowercase letters.
- It is `AB` (`A` followed by `B`), where `A` and `B` are both valid.
- It is `(A)`, where `A` is valid.

## Examples

**Example 1**

```
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
```

"lee(t(co)de)" and "lee(t(c)ode)" would also be accepted.

**Example 2**

```
Input: s = "a)b(c)d"
Output: "ab(c)d"
```

**Example 3**

```
Input: s = "))(("
Output: ""
```

An empty string is also valid.

## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is either `'('`, `')'`, or a lowercase English letter.

## Target complexity

O(n) time and O(n) space, where n is the length of `s`.

## Hints

<details><summary>Hint 1</summary>

Read the string from left to right and count open parentheses. At which moment do you know for sure that a `)` can't be kept?

</details>

<details><summary>Hint 2</summary>

Some `(` are only found to be bad when the string ends. You need to know where they were.

</details>

<details><summary>Hint 3</summary>

Building the answer by cutting one character out of a Python string at a time copies the string each time. With `n = 10^5` that is too slow.

</details>
