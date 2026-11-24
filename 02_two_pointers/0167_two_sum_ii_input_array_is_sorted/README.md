# 167. Two Sum II - Input Array Is Sorted

**Medium** · Array, Two Pointers, Binary Search ·
[NeetCode](https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150) ·
[LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

You get an array `numbers`, already sorted in non-decreasing order, and an integer `target`.
Find the two elements that add up to `target` and return their positions as `[index1, index2]`,
**1-indexed**, with `index1 < index2`. You can't use the same element twice, and there is
always exactly one valid pair.

Your solution must use `O(1)` extra space.

**Example 1**

```text
Input: numbers = [1,2,3,4], target = 3
Output: [1,2]
```

1 + 2 = 3, and with 1-based positions that's `[1, 2]`.

**Constraints**

- `2 <= numbers.length <= 30,000`
- `-1000 <= numbers[i] <= 1000`
- `-1000 <= target <= 1000`

<details><summary>Target complexity</summary>

`O(n)` time and `O(1)` space.

</details>

<details><summary>Hint 1</summary>

Trying every pair works, but on 30,000 elements that's about 450 million checks.

</details>

<details><summary>Hint 2</summary>

This is not the original Two Sum: the array is sorted. What does a sorted order let you rule out?

</details>

<details><summary>Hint 3</summary>

Watch the return format: positions start at 1, not 0.

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
