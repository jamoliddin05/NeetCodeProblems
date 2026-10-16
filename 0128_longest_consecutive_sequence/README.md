# 128. Longest Consecutive Sequence

**Medium** · Array, Hash Table, Union Find ·
[NeetCode](https://neetcode.io/problems/longest-consecutive-sequence/question) ·
[LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)

You get an integer array `nums`. Pick any of its values and line them up so that each one is
exactly `1` more than the one before — a consecutive run like `4, 5, 6, 7`. Return the length
of the longest run you can build. The values don't have to sit next to each other (or in
order) in `nums`, and a value that appears several times still counts once in a run. Your
algorithm has to run in `O(n)` time.

**Example 1**

```text
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].
```

**Example 2**

```text
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7
```

**Constraints**

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

<details><summary>Target complexity</summary>

`O(n)` time and `O(n)` space, where `n` is the size of the input array.

</details>

<details><summary>Hint 1</summary>

Sorting gives a correct answer, but it costs `O(n log n)`. Which structure answers "is the
value `x` somewhere in `nums`?" in `O(1)`?

</details>

<details><summary>Hint 2</summary>

Counting a run from every value you meet means a long run gets walked again and again — think
of a single run of `10^5` values. Is every value a sensible place to start counting?

</details>

<details><summary>Hint 3</summary>

Duplicates: `[1, 2, 2, 3]` has a run of length `3`, and a value repeated thousands of times
shouldn't make you repeat the same work thousands of times.

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
