# 518. Coin Change II

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/coin-change-ii/

## Task

You get a target `amount` and a list of different coin values `coins`. You can use each coin value
as many times as you like.

Return the number of different combinations of coins that add up to exactly `amount`. A
combination does not depend on order: `1 + 2` and `2 + 1` are the same combination. If no
combination adds up to `amount`, return `0`.

The answer always fits into a signed 32-bit integer.

Note the argument order: `amount` comes first, then `coins`.

## Examples

**Example 1**

```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2**

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3**

```
Input: amount = 10, coins = [10]
Output: 1
```

## Constraints

- `1 <= coins.length <= 300`
- `1 <= coins[i] <= 5000`
- All the values of `coins` are unique.
- `0 <= amount <= 5000`

## Hints

<details><summary>Hint 1</summary>

Counting ordered lists of coins gives too many: for `amount = 3`, `coins = [1, 2]` the answer is 2, not 3. How can you make sure each combination can be built in only one way?

</details>

<details><summary>Hint 2</summary>

Once you have decided how many coins of one value to use, that value never needs to be looked at again. What question is left about the other values?

</details>

<details><summary>Hint 3</summary>

What should the answer be for `amount = 0`?

</details>
