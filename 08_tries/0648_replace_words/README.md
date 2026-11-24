# 648. Replace Words

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/replace-words/

## Task

You get a list of roots `dictionary` and a `sentence` of words separated by single spaces. A word
that starts with a root is built from that root: for example, "helpful" starts with the root
"help".

Replace every word in the sentence that starts with some root by that root. If several roots fit
the same word, use the shortest one. Words that start with no root stay as they are. Return the new
sentence.

## Examples

**Example 1**

```
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

**Example 2**

```
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
```

## Constraints

- `1 <= dictionary.length <= 1000`
- `1 <= dictionary[i].length <= 100`
- `dictionary[i]` consists of only lower-case letters.
- `1 <= sentence.length <= 10^6`
- `sentence` consists of only lower-case letters and spaces.
- The number of words in `sentence` is in the range `[1, 1000]`
- The length of each word in `sentence` is in the range `[1, 1000]`
- Every two consecutive words in `sentence` will be separated by exactly one space.
- `sentence` does not have leading or trailing spaces.

## Target complexity

O(D + S) time, where D is the total length of all roots and S is the length of the sentence.

## Hints

<details><summary>Hint 1</summary>

For each word you need the shortest root that the word starts with. Does the order of the roots in
`dictionary` matter?

</details>

<details><summary>Hint 2</summary>

Comparing every word with every root can mean 1000 × 1000 comparisons. Can you read a word letter
by letter and learn, at each step, whether the letters so far form a root?

</details>

<details><summary>Hint 3</summary>

As soon as you find a root at the start of a word, longer roots no longer matter.

</details>
