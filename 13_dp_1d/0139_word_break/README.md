# 139. Word Break

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/word-break/

## Task

You get a string `s` and a list of words `wordDict`. Return `true` if `s` can be cut into pieces so
that every piece is a word from `wordDict`, and `false` otherwise.

The same word may be used any number of times.

## Examples

**Example 1**

```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

**Example 2**

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

**Example 3**

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

## Constraints

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are unique.

## Hints

<details><summary>Hint 1</summary>

Taking the longest word that matches at the start is not always right. In `"goalspecial"` with `["go", "goal", "goals", "special"]`, taking `"goals"` first leaves `"pecial"`, which cannot be cut into words.

</details>

<details><summary>Hint 2</summary>

Once a word has been matched up to position `i`, the rest of the work is the same question asked about the part of `s` from `i` on.

</details>

<details><summary>Hint 3</summary>

Many different ways of cutting the beginning of `s` end at the same position `i`. Does the answer for the part from `i` on depend on how you got to `i`?

</details>
