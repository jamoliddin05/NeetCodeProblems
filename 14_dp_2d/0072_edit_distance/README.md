# 72. Edit Distance

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/edit-distance/

## Task

You get two strings `word1` and `word2`. One operation is one of these:

- insert a character,
- delete a character,
- replace a character with another one.

Return the smallest number of operations that turns `word1` into `word2`.

## Examples

**Example 1**

```
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
```

**Example 2**

```
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
```

## Constraints

- `0 <= word1.length, word2.length <= 500`
- `word1` and `word2` consist of lowercase English letters.

## Hints

<details><summary>Hint 1</summary>

What is the answer when one of the two words is empty?

</details>

<details><summary>Hint 2</summary>

Look at the first characters of both words. If they are equal, do you need to do anything with them?

</details>

<details><summary>Hint 3</summary>

If they are different, each of the three operations deals with that first character in its own way. What is left to solve after each one?

</details>
