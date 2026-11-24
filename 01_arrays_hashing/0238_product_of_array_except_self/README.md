# 238. Product of Array Except Self

**Medium** · Array, Prefix Sum ·
[NeetCode](https://neetcode.io/problems/products-of-array-discluding-self/question) ·
[LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

You get an integer array `nums`. Return an array `output` of the same length in which
`output[i]` is the product of every element of `nums` except `nums[i]`. Every such product fits
in a 32-bit integer.

**Follow-up:** solve it in `O(n)` time **without using division**.

**Example 1**

```text
Input: nums = [1,2,4,6]
Output: [48,24,12,8]
```

**Example 2**

```text
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
```

**Constraints**

- `2 <= nums.length <= 100,000`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` fits in a 32-bit integer.

<details><summary>Target complexity</summary>

`O(n)` time and `O(n)` space, where `n` is the size of the input array.
LeetCode's version also asks for `O(1)` extra space, with the output array not counted.

</details>

<details><summary>Hint 1</summary>

The brute force multiplies `n - 1` numbers for each of the `n` positions. Two neighbouring
positions share almost all of that work. What exactly do they have in common?

</details>

<details><summary>Hint 2</summary>

Everything except `nums[i]` falls into two groups: the elements before `i` and the elements
after it. Can either group's product be carried along from one index to the next?

</details>

<details><summary>Hint 3</summary>

Check your answer on arrays with one zero and with two zeros. Those are the cases that make
the division shortcut awkward even where division is allowed.

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
