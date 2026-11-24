# 211. Design Add and Search Words Data Structure

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/design-add-and-search-words-data-structure/

## Task

Build a class `WordDictionary` that stores words and checks whether a pattern matches any of them:

- `WordDictionary()` creates an empty dictionary.
- `addWord(word)` stores `word`.
- `search(word)` returns `true` if some stored word matches `word`, `false` otherwise. The pattern
  `word` can contain dots `.`; each dot matches exactly one letter, any letter. All other characters
  must match exactly, and the stored word must have the same length as the pattern.

## Example

**Example 1**

```
Input: ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
       [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output: [null,null,null,null,false,true,true,true]
```

```
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

## Constraints

- `1 <= word.length <= 25`
- `word` in `addWord` consists of lowercase English letters.
- `word` in `search` consists of `'.'` or lowercase English letters.
- There will be at most `2` dots in `word` for `search` queries.
- At most `10^4` calls will be made to `addWord` and `search`.

## Target complexity

O(L) time for `addWord` and for a `search` without dots, where L is the length of the word.

## Hints

<details><summary>Hint 1</summary>

Without dots this is the same as `search` in problem 208, Implement Trie.

</details>

<details><summary>Hint 2</summary>

At a dot, more than one next letter can be right. Which ones do you have to try, and what do you do
when the first one you try leads nowhere?

</details>

<details><summary>Hint 3</summary>

A match has to use every character of the pattern and end exactly where a stored word ends.

</details>
