# 11. Container With Most Water

**Medium** · Array, Two Pointers, Greedy ·
[NeetCode](https://neetcode.io/problems/max-water-container/question?list=neetcode150) ·
[LeetCode](https://leetcode.com/problems/container-with-most-water/)

You get an integer array `heights`: `heights[i]` is the height of a vertical bar standing at
position `i`. Pick any two bars; together with the ground they form a container. The water it
holds is the distance between the two bars times the height of the lower one. Return the most
water any pair of bars can hold.

**Example 1**

```text
Input: height = [1,7,2,5,4,7,3,6]
Output: 36
```

The bars at positions 1 and 7 (heights 7 and 6) are 6 apart, and the lower one is 6 tall:
6 × 6 = 36. No other pair holds more.

**Example 2**

```text
Input: height = [2,2,2]
Output: 4
```

**Constraints**

- `2 <= height.length <= 100,000`
- `0 <= height[i] <= 10,000`

<details><summary>Target complexity</summary>

`O(n)` time and `O(1)` extra space, where `n` is the length of `heights`.

</details>

<details><summary>Hint 1</summary>

Trying every pair is `O(n^2)`: about 5 billion pairs at `n = 100,000`.

</details>

<details><summary>Hint 2</summary>

Which pair is the widest possible? Start there and ask what could make a narrower pair better.

</details>

<details><summary>Hint 3</summary>

Of the two bars in the current pair, one of them can't be part of any better answer. Which one,
and why?

</details>

---

Write your answer in `solution.py` and run that file: it runs every case from `inputs.txt`.
