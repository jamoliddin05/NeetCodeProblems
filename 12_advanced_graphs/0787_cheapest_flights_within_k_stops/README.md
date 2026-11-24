# 787. Cheapest Flights Within K Stops

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/cheapest-flights-within-k-stops/

## Task

There are `n` cities numbered from `0` to `n - 1`. You get a list `flights`, where
`flights[i] = [from, to, price]` is a one-way flight from city `from` to city `to` that costs
`price`.

You also get three integers `src`, `dst` and `k`. Return the lowest total price of a trip from
`src` to `dst` that makes at most `k` stops, where a stop is a city you land in between `src` and
`dst`. So a trip with at most `k` stops uses at most `k + 1` flights. If no such trip exists,
return `-1`.

## Examples

**Example 1**

```
Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
```

The cheapest trip with at most 1 stop is `0 -> 1 -> 3`, costing 100 + 600 = 700. The trip
`0 -> 1 -> 2 -> 3` costs only 400, but it makes 2 stops, so it is not allowed.

**Example 2**

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
```

The cheapest trip with at most 1 stop is `0 -> 1 -> 2`, costing 100 + 100 = 200.

**Example 3**

```
Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
```

With no stops allowed, the only trip is the direct flight `0 -> 2` for 500.

## Constraints

- `2 <= n <= 100`
- `0 <= flights.length <= (n * (n - 1) / 2)`
- `flights[i].length == 3`
- `0 <= from, to < n`
- `from != to`
- `1 <= price <= 10^4`
- There are no repeated flights between the same two cities.
- `0 <= src, dst, k < n`
- `src != dst`

## Target complexity

O(n + k * m) time and O(n) space, where m is the length of `flights`.

## Hints

<details><summary>Hint 1</summary>

The cheapest way to reach a city and the way with the fewest flights can be different trips. Your
solution has to keep track of both the price and the number of flights used.

</details>

<details><summary>Hint 2</summary>

What is the cheapest price to each city using at most 1 flight? How do you get the answer for at
most 2 flights from the answer for at most 1 flight?

</details>

<details><summary>Hint 3</summary>

A cheap way into a city can use up all the allowed stops, while a pricier way into the same city
with fewer stops can still lead to `dst`. Make sure your solution does not throw the second one
away.

</details>
