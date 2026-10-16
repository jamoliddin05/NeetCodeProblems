# 49. Group Anagrams

**Medium** · Array, Hash Table, String, Sorting ·
[NeetCode](https://neetcode.io/problems/anagram-groups/question?list=neetcode150) ·
[LeetCode](https://leetcode.com/problems/group-anagrams/)

You get a list of strings `strs`. Put every string into a group with all of its anagrams
(strings made of exactly the same letters, each the same number of times) and return the list
of groups. Every string from the input appears in exactly one group, repeats included. The
order of the groups, and of the strings inside a group, doesn't matter.

**Example 1**

```text
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
```

**Example 2**

```text
Input: strs = ["x"]
Output: [["x"]]
```

**Example 3**

```text
Input: strs = [""]
Output: [[""]]
```

**Constraints**

- `1 <= strs.length <= 10,000`
- `0 <= strs[i].length <= 100`
- `strs[i]` is made up of lowercase English letters.

<details><summary>Target complexity</summary>

`O(m * n)` time and `O(m)` space, where `m` is the number of strings and `n` is the length of
the longest string.

</details>

<details><summary>Hint 1</summary>

Comparing every string with every other string is too slow at 10^4 strings. Each string should
be looked at only a constant number of times.

</details>

<details><summary>Hint 2</summary>

What could you compute from a single word that comes out exactly the same for all of its
anagrams, and different for every non-anagram?

</details>

<details><summary>Hint 3</summary>

Once each word has such a "signature", grouping is a dictionary job. Remember which types can
be dictionary keys.

</details>

<details><summary>Hint 4</summary>

Make sure two different groups can never get the same signature: `"ad"` and `"bc"` have equal
sums of letter codes, and numbers glued together without a separator can be ambiguous
(`1` and `11` vs `11` and `1`).

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
