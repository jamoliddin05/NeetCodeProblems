# 271. Encode and Decode Strings

**Medium** · Array, String, Design ·
[NeetCode](https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150) ·
[LeetCode](https://leetcode.com/problems/encode-and-decode-strings/) (Premium)

Write two methods. `encode` turns a list of strings into one string; `decode` turns that string
back into the exact original list: same number of strings, same order, every character intact.
Picture `encode` running on one machine and `decode` on another, with only the encoded string
sent between them, so `decode` can't rely on anything stored in the object. The tests call each
method on its own `Solution()` for that reason.

**Example 1**

```text
Input: strs = ["Hello","World"]
Output: ["Hello","World"]
```

**Example 2**

```text
Input: strs = [""]
Output: [""]
```

**Constraints**

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains any possible characters out of 256 valid ASCII characters.

**Follow-up:** could your algorithm work for any possible set of characters?

<details><summary>Target complexity</summary>

`O(m)` time for each `encode()` and `decode()` call and `O(m + n)` space, where `m` is the total
length of all the strings and `n` is the number of strings.

</details>

<details><summary>Hint 1</summary>

Any character can appear inside the strings, including any separator you might pick. A scheme
that relies on "this character never shows up" will break.

</details>

<details><summary>Hint 2</summary>

Write down what `[]`, `[""]` and `["", ""]` should encode to. The decoder has to tell all three
apart.

</details>

<details><summary>Hint 3</summary>

If the decoder knew exactly how much of the string belongs to the next item before reading it,
would it matter what characters were inside?

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
