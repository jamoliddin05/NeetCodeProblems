# 371. Sum of Two Integers

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/sum-of-two-integers/

## Task

You get two integers `a` and `b`. Return their sum, without using the operators `+` and `-`.

## Examples

**Example 1**

```
Input: a = 1, b = 2
Output: 3
```

**Example 2**

```
Input: a = 2, b = 3
Output: 5
```

## Constraints

- `-1000 <= a, b <= 1000`

## Hints

<details><summary>Hint 1</summary>

Add two numbers in binary on paper. In one column, the result bit and the carry bit depend only on
the two input bits. Which bitwise operation gives each of them?

</details>

<details><summary>Hint 2</summary>

The carries still have to be added, and adding them can make new carries. When does that stop?

</details>

<details><summary>Hint 3</summary>

Try `a = -1, b = 1`. In C++ or Java an int has exactly 32 bits, but a Python int has no fixed size,
and a negative one behaves as if it had an endless row of 1 bits on the left. Does your loop still
finish?

</details>
