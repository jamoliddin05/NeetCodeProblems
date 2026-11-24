# 201. Bitwise AND of Numbers Range

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/bitwise-and-of-numbers-range/

## Task

You get two integers `left` and `right`. Return the bitwise AND of all integers from `left` to
`right`, both included.

## Examples

**Example 1**

```
Input: left = 5, right = 7
Output: 4
```

**Example 2**

```
Input: left = 0, right = 0
Output: 0
```

**Example 3**

```
Input: left = 1, right = 2147483647
Output: 0
```

## Constraints

- `0 <= left <= right <= 2^31 - 1`

## Hints

<details><summary>Hint 1</summary>

The range can hold about two billion numbers, so going through all of them is too slow.

</details>

<details><summary>Hint 2</summary>

Write `left` and `right` in binary, one under the other. If some bit changes from 0 to 1 or from 1 to
0 anywhere in the range, what is that bit in the answer?

</details>

<details><summary>Hint 3</summary>

Which bits stay the same for every number from `left` to `right`?

</details>
