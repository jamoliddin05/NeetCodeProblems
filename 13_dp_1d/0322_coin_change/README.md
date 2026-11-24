# 322. Coin Change

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/coin-change/

## Task

You get a list of coin values `coins` and a target `amount`. You can use each coin value as many
times as you like.

Return the smallest number of coins whose values add up to exactly `amount`. If no set of coins
adds up to `amount`, return `-1`.

## Examples

**Example 1**

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

**Example 2**

```
Input: coins = [2], amount = 3
Output: -1
```

**Example 3**

```
Input: coins = [1], amount = 0
Output: 0
```

## Constraints

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Hints

<details><summary>Hint 1</summary>

Always taking the largest coin that still fits does not work. Try `coins = [1, 3, 4]`, `amount = 6`.

</details>

<details><summary>Hint 2</summary>

Whatever the best set of coins is, one of its coins can be counted last. If that coin is `c`, what is left to solve?

</details>

<details><summary>Hint 3</summary>

How many different remaining amounts can come up at most? Does it make sense to solve the same one twice?

</details>
