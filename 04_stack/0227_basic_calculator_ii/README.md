# 227. Basic Calculator II

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/basic-calculator-ii/

## Task

You get a string `s` that holds an arithmetic expression with non-negative integers and the
operators `+`, `-`, `*` and `/`, possibly with spaces between them. Compute it and return the result.

Details:

- `*` and `/` are done before `+` and `-`, and operators of the same kind go from left to right.
- Integer division truncates toward zero.
- The expression is always valid, and every intermediate result fits in `[-2^31, 2^31 - 1]`.
- You may not use any built-in function that evaluates a string as math, such as `eval()`.

## Examples

**Example 1**

```
Input: s = "3+2*2"
Output: 7
```

**Example 2**

```
Input: s = " 3/2 "
Output: 1
```

**Example 3**

```
Input: s = " 3+5 / 2 "
Output: 5
```

## Constraints

- `1 <= s.length <= 3 * 10^5`
- `s` consists of integers and operators (`'+'`, `'-'`, `'*'`, `'/'`) separated by some number of spaces.
- `s` represents a valid expression.
- All the integers in the expression are non-negative integers in the range `[0, 2^31 - 1]`.
- The answer is guaranteed to fit in a 32-bit integer.

## Target complexity

O(n) time, where n is the length of `s`.

## Hints

<details><summary>Hint 1</summary>

Numbers can have many digits, and spaces can be anywhere between the tokens.

</details>

<details><summary>Hint 2</summary>

When you read `a + b`, you can't add yet: a `*` or `/` may come right after `b`. What can you do with `a` for now, and when is it safe to use it?

</details>

<details><summary>Hint 3</summary>

Try `"1-3/2"`; the answer is `0`. Python's `//` rounds toward negative infinity, which matters as soon as a negative number is divided.

</details>
