# 13. Roman to Integer

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/roman-to-integer/

## Task

Roman numerals use seven symbols:

| Symbol | Value |
|---|---|
| `I` | 1 |
| `V` | 5 |
| `X` | 10 |
| `L` | 50 |
| `C` | 100 |
| `D` | 500 |
| `M` | 1000 |

A numeral is usually written from the largest symbol to the smallest, and its value is the sum of
its symbols: `II` is 2, `XII` is 10 + 2 = 12, `XXVII` is 20 + 5 + 2 = 27.

Six pairs are written in the opposite order. When one of these smaller symbols stands right before
the larger one, it is subtracted instead of added:

- `IV` = 4 and `IX` = 9
- `XL` = 40 and `XC` = 90
- `CD` = 400 and `CM` = 900

You get a valid Roman numeral `s`. Return its value as an integer.

## Examples

**Example 1**

```
Input: s = "III"
Output: 3
```

III = 3.

**Example 2**

```
Input: s = "LVIII"
Output: 58
```

L = 50, V = 5, III = 3.

**Example 3**

```
Input: s = "MCMXCIV"
Output: 1994
```

M = 1000, CM = 900, XC = 90 and IV = 4.

## Constraints

- `1 <= s.length <= 15`
- `s` contains only the characters `'I'`, `'V'`, `'X'`, `'L'`, `'C'`, `'D'` and `'M'`.
- `s` is guaranteed to be a valid Roman numeral in the range `[1, 3999]`.

## Hints

<details><summary>Hint 1</summary>

Write the value of each symbol of `MCMXCIV` under it: 1000, 100, 1000, 10, 100, 1, 5. Which of these
numbers are added to the answer and which are subtracted?

</details>

<details><summary>Hint 2</summary>

A symbol is subtracted only in one situation. Which other symbol do you need to look at to know
whether it happens?

</details>

<details><summary>Hint 3</summary>

Reading the string from the last symbol to the first can make that check simpler.

</details>
