# 78. Subsets

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/subsets/

## Task

You get an integer array `nums` whose elements are all different. Return all of its subsets
(the power set), including the empty one and the whole array.

The answer must not contain the same subset twice. The subsets can be returned in any order.

## Examples

**Example 1**

```
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

**Example 2**

```
Input: nums = [0]
Output: [[],[0]]
```

## Constraints

- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
- All the numbers of `nums` are **unique**.

## Hints

<details><summary>Hint 1</summary>

How many subsets does an array of `n` elements have? Your answer should have exactly that many.

</details>

<details><summary>Hint 2</summary>

Look at one element on its own. In how many ways can it relate to a subset?

</details>

<details><summary>Hint 3</summary>

If you build subsets in a shared list that you change as you go, make sure that what you add to the answer is a copy.

</details>
