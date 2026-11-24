# 208. Implement Trie (Prefix Tree)

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/implement-trie-prefix-tree/

## Task

A trie (prefix tree) is a tree that stores strings so that words with the same beginning share the
storage for that beginning. It is used for things like autocomplete and spell checking.

Build a class `Trie` with:

- `Trie()` creates an empty trie.
- `insert(word)` stores the string `word`.
- `search(word)` returns `true` if `word` itself was stored earlier, `false` otherwise.
- `startsWith(prefix)` returns `true` if some stored word starts with `prefix`, `false` otherwise.

## Example

**Example 1**

```
Input: ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
       [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output: [null, null, true, false, true, null, true]
```

```
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

## Constraints

- `1 <= word.length, prefix.length <= 2000`
- `word` and `prefix` consist only of lowercase English letters.
- At most `3 * 10^4` calls in total will be made to `insert`, `search`, and `startsWith`.

## Target complexity

O(L) time for each call, where L is the length of `word` or `prefix`.

## Hints

<details><summary>Hint 1</summary>

Words that begin with the same letters, such as "car" and "cat", can share the part for "ca".

</details>

<details><summary>Hint 2</summary>

After you follow all letters of "app" while "apple" is stored, how do you tell "a stored word ends
here" from "a stored word only passes through here"?

</details>

<details><summary>Hint 3</summary>

`search` and `startsWith` walk through the letters in the same way. They differ only in what they
check at the end.

</details>
