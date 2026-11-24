# 15. 3Sum

**Medium** · Array, Two Pointers, Sorting ·
[NeetCode](https://neetcode.io/problems/three-integer-sum/question?list=neetcode150) ·
[LeetCode](https://leetcode.com/problems/3sum/)

You get an integer array `nums`. Return every triplet `[nums[i], nums[j], nums[k]]` that adds up
to `0`, where `i`, `j` and `k` are three different positions. The same triplet of values must
not appear twice in the answer. The triplets can come in any order, and so can the numbers inside
each one.

**Example 1**

```text
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

Three combinations of positions add up to zero, but they give only two different triplets.

**Example 2**

```text
Input: nums = [0,1,1]
Output: []
```

The only possible triplet doesn't add up to zero.

**Example 3**

```text
Input: nums = [0,0,0]
Output: [[0,0,0]]
```

The only possible triplet adds up to zero.

**Constraints**

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

<details><summary>Target complexity</summary>

`O(n^2)` time and `O(1)` extra space, where `n` is the length of `nums`.

</details>

<details><summary>Hint 1</summary>

Checking every triplet is `O(n^3)`: about 4.5 billion checks at `n = 3000`.

</details>

<details><summary>Hint 2</summary>

Fix one number. What do the other two have to add up to? Have you solved that smaller problem
before?

</details>

<details><summary>Hint 3</summary>

Collecting everything into a set of tuples removes duplicates, but it's the slow way. Think
about how equal values could sit next to each other.

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
