# 692. Top K Frequent Words

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/top-k-frequent-words/

## Task

You get an array of strings `words` and an integer `k`. Return the `k` words that appear most
often.

The order of the answer is fixed: sort by frequency from highest to lowest, and sort words with
the same frequency in lexicographical (alphabetical) order.

## Examples

**Example 1**

```
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
```

"i" and "love" are the two most frequent words. Note that "i" comes before "love" because it is
earlier in alphabetical order.

**Example 2**

```
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
```

"the", "is", "sunny" and "day" are the four most frequent words, with 4, 3, 2 and 1 occurrences
respectively.

## Constraints

- `1 <= words.length <= 500`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- `k` is in the range `[1, The number of **unique** words[i]]`

## Follow-up

Could you solve it in `O(n log(k))` time and `O(n)` extra space?

## Hints

<details><summary>Hint 1</summary>

Start by finding out how many times each distinct word appears.

</details>

<details><summary>Hint 2</summary>

The answer is ordered by two keys at once. Write down exactly when one word must come before another.

</details>

<details><summary>Hint 3</summary>

Words with the same frequency are where most wrong answers come from. Check every place where your code compares two words.

</details>
