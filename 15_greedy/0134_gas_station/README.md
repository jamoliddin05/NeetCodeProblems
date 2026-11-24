# 134. Gas Station

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/gas-station/

## Task

There are `n` gas stations on a circular road. At station `i` you can take `gas[i]` units of
gas. Driving from station `i` to the next station uses `cost[i]` units; after the last station
the road leads back to station `0`. Your car's tank has no size limit, and it is empty at the
start.

You pick one station to start from, take its gas, and drive clockwise, taking all the gas at
every station you reach. You can drive a stretch of road only if the tank holds at least its
cost when you leave the station.

Return the index of the station from which you can drive around the whole circle once and come
back to it, or `-1` if there is no such station. If such a station exists, it is unique.

## Examples

**Example 1**

```
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
```

Start at station 3 and take 4 units: the tank holds 4.

- Drive to station 4: 4 - 1 + 5 = 8.
- Drive to station 0: 8 - 2 + 1 = 7.
- Drive to station 1: 7 - 3 + 2 = 6.
- Drive to station 2: 6 - 4 + 3 = 5.
- Drive to station 3: this costs 5 and the tank holds 5, so you make it back.

**Example 2**

```
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
```

Stations 0 and 1 don't give enough gas for their first stretch. Starting at station 2 you reach
station 0 with 4 - 3 + 2 = 3 units and station 1 with 3 - 3 + 3 = 3 units, but the stretch back
to station 2 costs 4.

## Constraints

- `n == gas.length == cost.length`
- `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`
- The input is built so that the answer is unique.

## Target complexity

O(n) time and O(1) extra space.

## Hints

<details><summary>Hint 1</summary>

Trying every start and driving the full circle from it is O(n^2): 10^10 steps for n = 10^5.

</details>

<details><summary>Hint 2</summary>

If all the gas on the road adds up to less than all the costs, can any start work? And if it
doesn't?

</details>

<details><summary>Hint 3</summary>

Say you start at station `a` and first run out of gas on the way to station `b`. What does that
tell you about the stations between `a` and `b` as starting points?

</details>
