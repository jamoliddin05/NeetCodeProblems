# 20. Valid Parentheses

**Difficulty:** Easy
**NeetCode:** https://neetcode.io/problems/validate-parentheses/question?list=neetcode150
**LeetCode:** https://leetcode.com/problems/valid-parentheses/

## Task

You get a string `s` that contains only the characters `(`, `)`, `{`, `}`, `[` and `]`.
Return `true` if the brackets in it are valid, `false` otherwise.

The string is valid when all three hold:

1. Every opening bracket is closed by a closing bracket of the same type.
2. Opening brackets are closed in the correct order.
3. Every closing bracket has a matching opening bracket of the same type before it.

## Examples

**Example 1**

```
Input: s = "[]"
Output: true
```

**Example 2**

```
Input: s = "([{}])"
Output: true
```

**Example 3**

```
Input: s = "[(])"
Output: false
```

The brackets are not closed in the correct order.

## Constraints

- `1 <= s.length <= 1000`

## Target complexity

O(n) time and O(n) space, where n is the length of the string.

## Hints

<details><summary>Hint 1</summary>

When you read a closing bracket, which opening bracket must it close? Not any open one, only one specific one.

</details>

<details><summary>Hint 2</summary>

The opening bracket that must be closed next is always the one opened most recently that is still open.

</details>

<details><summary>Hint 3</summary>

After the whole string is read, what must be true about the brackets still open?

</details>
