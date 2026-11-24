# 347. Top K Frequent Elements

**Medium** · Array, Hash Table, Sorting, Bucket Sort, Heap ·
[NeetCode](https://neetcode.io/problems/top-k-elements-in-list/question) ·
[LeetCode](https://leetcode.com/problems/top-k-frequent-elements/)

You get an integer array `nums` and an integer `k`. Return the `k` values that occur in `nums`
most often. The tests are built so that exactly one set of `k` values is correct (no tie at the
cut-off point), and the values may be returned in any order.

**Example 1**

```text
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]
```

**Example 2**

```text
Input: nums = [7,7], k = 1
Output: [7]
```

**Constraints**

- `1 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`
- `1 <= k <= number of distinct elements in nums`

<details><summary>Target complexity</summary>

`O(n)` time and `O(n)` space, where `n` is the size of the input array.

</details>

<details><summary>Hint 1</summary>

Before you can pick the "most frequent" values, you need to know how often each value occurs.
How cheaply can you get that for every value at once?

</details>

<details><summary>Hint 2</summary>

Sorting everything works but is `O(n log n)`. Note that a frequency can never be larger than
`n` — does a small, bounded range of keys suggest a way to order things without comparing them?

</details>

<details><summary>Hint 3</summary>

Several values can share the same frequency, and `k` counts values, not distinct frequencies.

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
