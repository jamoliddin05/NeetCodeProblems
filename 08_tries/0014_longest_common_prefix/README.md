# 14. Longest Common Prefix

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/longest-common-prefix/

## Task

You get a list of strings `strs`. Return the longest string that every one of them starts with.
If they have no common start at all, return the empty string `""`.

## Examples

**Example 1**

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2**

```
Input: strs = ["dog","racecar","car"]
Output: ""
```

There is no common prefix among the input strings.

## Constraints

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

## Target complexity

O(S) time, where S is the total number of characters in all strings.

## Hints

<details><summary>Hint 1</summary>

The answer can't be longer than the shortest string in the list.

</details>

<details><summary>Hint 2</summary>

Compare the strings one position at a time. What has to happen at a position for you to stop?

</details>

<details><summary>Hint 3</summary>

A single empty string in the list makes the answer empty.

</details>
