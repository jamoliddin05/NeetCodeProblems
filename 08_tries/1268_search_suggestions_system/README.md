# 1268. Search Suggestions System

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/search-suggestions-system/

## Task

You get a list of product names `products` and a string `searchWord` that a user types one letter
at a time.

After each typed letter, suggest up to three products that start with the letters typed so far.
If more than three products start with them, suggest the three that come first in alphabetical
(lexicographic) order, listed in that order.

Return a list with one list of suggestions per typed letter. When no product starts with the typed
letters, that list is empty.

## Examples

**Example 1**

```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]
```

Products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].

**Example 2**

```
Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
```

The only word "havana" will be always suggested while typing the search word.

## Constraints

- `1 <= products.length <= 1000`
- `1 <= products[i].length <= 3000`
- `1 <= sum(products[i].length) <= 2 * 10^4`
- All the strings of `products` are unique.
- `products[i]` consists of lowercase English letters.
- `1 <= searchWord.length <= 1000`
- `searchWord` consists of lowercase English letters.

## Target complexity

O(S log n + m) time, where n is the number of products, S is their total length and m is the
length of `searchWord`.

## Hints

<details><summary>Hint 1</summary>

If the products were in alphabetical order, where would all products that start with a given set
of letters be?

</details>

<details><summary>Hint 2</summary>

When one more letter is typed, the matching products are a part of the products that matched
before.

</details>

<details><summary>Hint 3</summary>

Once no product matches the typed letters, no product can match after more letters are typed.

</details>
