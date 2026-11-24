# 767. Reorganize String

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/reorganize-string/

## Task

You get a string `s`. Rearrange its characters so that no two neighbouring characters are the
same.

Return any such rearrangement, or `""` if it is not possible.

## Examples

**Example 1**

```
Input: s = "aab"
Output: "aba"
```

**Example 2**

```
Input: s = "aaab"
Output: ""
```

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Hints

<details><summary>Hint 1</summary>

Count each letter first. When is a rearrangement impossible? Think about the letter that appears most often and the length of the string.

</details>

<details><summary>Hint 2</summary>

Each time you place a letter, which letter is the most dangerous to leave for later?

</details>

<details><summary>Hint 3</summary>

The letter you just placed cannot be placed again right away. How do you keep it out of the choice for one step and then bring it back?

</details>
