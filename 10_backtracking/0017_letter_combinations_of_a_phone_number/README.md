# 17. Letter Combinations of a Phone Number

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## Task

You get a string `digits` made of the digits `2` to `9`. Each digit stands for the letters on
its telephone button. Return every string of letters that the digits could spell, in any order.

The digit-to-letter mapping (the digit `1` has no letters):

| Digit | Letters |
|---|---|
| 2 | abc |
| 3 | def |
| 4 | ghi |
| 5 | jkl |
| 6 | mno |
| 7 | pqrs |
| 8 | tuv |
| 9 | wxyz |

## Examples

**Example 1**

```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

**Example 2**

```
Input: digits = "2"
Output: ["a","b","c"]
```

## Constraints

- `1 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

## Hints

<details><summary>Hint 1</summary>

How many strings should the answer have? It depends only on how many letters each digit has.

</details>

<details><summary>Hint 2</summary>

Each string has one letter per digit, in the same order as the digits. Choose the letters one position at a time.

</details>

<details><summary>Hint 3</summary>

Not every button has three letters.

</details>
