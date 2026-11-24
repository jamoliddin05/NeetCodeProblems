# 50. Pow(x, n)

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/powx-n/

## Task

Write your own `pow(x, n)`: return the number `x` raised to the integer power `n`, that is
x<sup>n</sup>. The power `n` can be positive, zero or negative.

The answer is a float. It counts as correct when it differs from the exact value by at most a
relative error of `10^-5`.

## Examples

**Example 1**

```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

**Example 2**

```
Input: x = 2.10000, n = 3
Output: 9.26100
```

**Example 3**

```
Input: x = 2.00000, n = -2
Output: 0.25000
```

2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25.

## Constraints

- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`
- `n` is an integer.
- Either `x` is not zero or `n > 0`.
- `-10^4 <= x^n <= 10^4`

## Hints

<details><summary>Hint 1</summary>

`n` can be about two billion, so multiplying by `x` one time after another is too slow.

</details>

<details><summary>Hint 2</summary>

If you already know x<sup>k</sup>, which larger power can you get with a single multiplication?

</details>

<details><summary>Hint 3</summary>

How does a negative `n` change the answer? Make sure your idea also works for `n = -2^31`.

</details>
