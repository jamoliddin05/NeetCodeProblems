# 150. Evaluate Reverse Polish Notation

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/evaluate-reverse-polish-notation/

## Task

You get an array of strings `tokens` that holds an arithmetic expression in Reverse Polish
Notation: each operator is written after its two operands, so `["2", "1", "+"]` means `2 + 1`.
Compute the expression and return the result as an integer.

Details:

- The operators are `"+"`, `"-"`, `"*"` and `"/"`.
- Each operand is an integer or the result of another expression.
- Division between two integers truncates toward zero (`7 / -2` is `-3`, not `-4`).
- There is never a division by zero.
- The input is always a valid expression.
- The answer and every intermediate result fit in a 32-bit integer.

## Examples

**Example 1**

```
Input: tokens = ["2","1","+","3","*"]
Output: 9
```

((2 + 1) * 3) = 9

**Example 2**

```
Input: tokens = ["4","13","5","/","+"]
Output: 6
```

(4 + (13 / 5)) = 6

**Example 3**

```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
```

```
((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

## Constraints

- `1 <= tokens.length <= 10^4`
- `tokens[i]` is either an operator: `"+"`, `"-"`, `"*"` or `"/"`, or an integer in the range `[-200, 200]`.

## Target complexity

O(n) time and O(n) space, where n is the length of `tokens`.

## Hints

<details><summary>Hint 1</summary>

When you reach an operator, which two numbers does it work on? Where in the tokens read so far are they?

</details>

<details><summary>Hint 2</summary>

After an operator is applied, its result becomes an operand for a later operator, just like a number from the input.

</details>

<details><summary>Hint 3</summary>

Python's `//` rounds toward negative infinity, so `-7 // 2` is `-4`. The task wants `-3`. Also check the operand order for `-` and `/`.

</details>
