# 42. Trapping Rain Water

**Hard** · Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack ·
[NeetCode](https://neetcode.io/problems/trapping-rain-water/question?list=neetcode150) ·
[LeetCode](https://leetcode.com/problems/trapping-rain-water/)

You get an array `height` of non-negative integers: an elevation map where each bar is 1 unit
wide and `height[i]` units tall. Rain falls on it. Return how many units of water stay trapped
between the bars once it settles. Water that isn't held in on both sides runs off the edges.

**Example 1**

```text
Input: height = [0,2,0,3,1,0,1,3,2,1]
Output: 9
```

**Constraints**

- `1 <= height.length <= 20,000`
- `0 <= height[i] <= 100,000`

<details><summary>Target complexity</summary>

`O(n)` time and `O(n)` space or better, where `n` is the length of `height`.

</details>

<details><summary>Hint 1</summary>

Forget the whole map for a moment. How much water sits on top of one bar `i`, and what does
that depend on?

</details>

<details><summary>Hint 2</summary>

Answering hint 1 by scanning outward from every bar works, but it's `O(n^2)`: 400 million steps
at `n = 20,000`. Which part of that scan keeps getting repeated?

</details>

<details><summary>Hint 3</summary>

Draw Example 1 on paper and fill in the water. Then check which bars actually decided each
water level.

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
