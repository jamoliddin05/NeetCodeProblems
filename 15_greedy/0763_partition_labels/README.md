# 763. Partition Labels

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/partition-labels/

## Task

You get a string `s`. Cut it into as many parts as possible so that each letter appears in at
most one part. You only cut: putting the parts back together in order must give `s` again.

For example, `"ababcc"` can be cut into `["abab", "cc"]`. The cut `["aba", "bcc"]` is not
allowed, because `b` is in both parts, and neither is `["ab", "ab", "cc"]`.

Return a list with the length of each part, in order.

## Examples

**Example 1**

```
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
```

The parts are `"ababcbaca"`, `"defegde"` and `"hijhklij"`. Cutting into `"ababcbacadefegde"` and
`"hijhklij"` also keeps every letter in one part, but gives fewer parts.

**Example 2**

```
Input: s = "eccbbbbdec"
Output: [10]
```

## Constraints

- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.

## Target complexity

O(n) time and O(1) extra space (there are only 26 letters), where n is the length of `s`.

## Hints

<details><summary>Hint 1</summary>

Look at the first letter of `s`. What is the earliest place where the first part could end?

</details>

<details><summary>Hint 2</summary>

Other letters between the start of the part and that place can push the end of the part further
to the right. When does the end stop moving?

</details>
