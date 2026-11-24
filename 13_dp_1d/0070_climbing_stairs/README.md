# 70. Climbing Stairs

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/climbing-stairs/

## Task

A staircase has `n` steps. With each move you go up either 1 step or 2 steps.
Return the number of different ways to reach the top.

Two ways are different when their lists of moves are different, so `1 + 2` and `2 + 1` count as
two ways.

## Examples

**Example 1**

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

**Example 2**

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Constraints

- `1 <= n <= 45`

## Hints

<details><summary>Hint 1</summary>

Look at the last move, the one that lands on step `n`. Where could you have been standing just before it?

</details>

<details><summary>Hint 2</summary>

Count the ways for `n = 1, 2, 3, 4, 5` by hand. How is each answer related to the answers before it?

</details>

<details><summary>Hint 3</summary>

A solution that works out the same smaller staircase many times will not finish for `n = 45`. Does any smaller staircase need to be worked out more than once?

</details>
