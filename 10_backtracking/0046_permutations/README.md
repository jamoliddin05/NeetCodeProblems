# 46. Permutations

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/permutations/

## Task

You get an array `nums` of distinct integers. Return all possible orderings (permutations) of
its elements. The permutations can be returned in any order.

## Examples

**Example 1**

```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

**Example 2**

```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```

**Example 3**

```
Input: nums = [1]
Output: [[1]]
```

## Constraints

- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`
- All the integers of `nums` are **unique**.

## Hints

<details><summary>Hint 1</summary>

How many permutations does an array of `n` distinct elements have? Your answer should have exactly that many.

</details>

<details><summary>Hint 2</summary>

Fill the positions one at a time. For the current position, which elements are still allowed?

</details>

<details><summary>Hint 3</summary>

If you build a permutation in a shared list that you change as you go, make sure that what you add to the answer is a copy.

</details>
