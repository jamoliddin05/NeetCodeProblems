# 567. Permutation in String

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/permutation-in-string/

## Task

You get two strings `s1` and `s2`. Return `true` if some substring of `s2` is a permutation of
`s1`, and `false` otherwise.

A permutation of `s1` is any string made of exactly the same letters as `s1`, each used the
same number of times, in any order. A substring is a block of characters that stand next to each
other in `s2`.

## Examples

**Example 1**

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
```

`s2` contains one permutation of `s1` ("ba").

**Example 2**

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

## Constraints

- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.

## Target complexity

O(n) time and O(1) extra space (only 26 letters), where n is the length of `s2`.

## Hints

<details><summary>Hint 1</summary>

How long must a substring of `s2` be to have a chance of being a permutation of `s1`?

</details>

<details><summary>Hint 2</summary>

How can you tell that two strings are permutations of each other without trying every order of letters?

</details>

<details><summary>Hint 3</summary>

Two substrings that start one position apart share almost all of their letters. Rebuilding the check from scratch for each one repeats work.

</details>
