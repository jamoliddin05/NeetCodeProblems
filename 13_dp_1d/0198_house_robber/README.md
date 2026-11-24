# 198. House Robber

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/house-robber/

## Task

Houses stand in a row along a street, and `nums[i]` is the amount of money in house `i`.
You want to take money from some of the houses, but you can never take from two houses that are
next to each other: their alarms are linked and would call the police.

Return the largest total amount of money you can take.

## Examples

**Example 1**

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

**Example 2**

```
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

## Hints

<details><summary>Hint 1</summary>

Taking every other house (all even positions, or all odd positions) is not always best. Try `[2, 1, 1, 2]`.

</details>

<details><summary>Hint 2</summary>

For the last house there are only two choices: take it or leave it. What does each choice allow for the houses before it?

</details>

<details><summary>Hint 3</summary>

Trying every allowed set of houses is far too slow for 100 houses. Does the best total for the first `i` houses depend on which houses you will pick after them?

</details>
