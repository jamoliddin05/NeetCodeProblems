# 43. Multiply Strings

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/multiply-strings/

## Task

You get two non-negative integers `num1` and `num2`, each written as a string of digits. Return
their product, also written as a string of digits.

You must not use a big-integer library, and you must not turn the inputs into integers directly
(no `int(num1)`). Work with the digits yourself.

## Examples

**Example 1**

```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2**

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

## Constraints

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` contain only digits.
- Neither `num1` nor `num2` has a leading zero, except the number `0` itself.

## Hints

<details><summary>Hint 1</summary>

Think of how you multiply two numbers on paper. How many digits can the product have at most?

</details>

<details><summary>Hint 2</summary>

Count digit positions from the right, starting at 0. When you multiply the digit at position `i` of
one number by the digit at position `j` of the other, which position of the product does that
result belong to?

</details>

<details><summary>Hint 3</summary>

The answer must not start with `0`, unless the whole answer is `"0"`.

</details>
