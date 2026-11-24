# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Task

You get an array `prices`, where `prices[i]` is the price of one stock on day `i`.
You may buy the stock on one day and sell it on a later day, once.

Return the largest profit (sell price minus buy price) you can make this way.
If no choice of days gives a profit above zero, return `0`.

## Examples

**Example 1**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
```

Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Buying on day 2 and selling on day 1 is not allowed, because you must buy before you sell.

**Example 2**

```
Input: prices = [7,6,4,3,1]
Output: 0
```

The price only falls, so no transaction is made and the profit is 0.

## Constraints

- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Target complexity

O(n) time and O(1) extra space, where n is the length of `prices`.

## Hints

<details><summary>Hint 1</summary>

Fix the day you sell on. Which buy day is the best one for it?

</details>

<details><summary>Hint 2</summary>

Checking every buy day for every sell day is O(n^2), which is 5 * 10^9 pairs at the largest size. What do you need to remember about the days already seen to answer Hint 1 at once?

</details>

<details><summary>Hint 3</summary>

The lowest price of all may come after the highest price. Look at `[2, 10, 1, 4]`.

</details>
