# 260. Single Number III

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/single-number-iii/

## Task

You get an integer array `nums`. Exactly two values in it appear only once, and every other value
appears exactly twice. Return the two values that appear once, in any order.

Your solution must run in linear time and use only constant extra space.

## Examples

**Example 1**

```
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
```

[5, 3] is also a valid answer.

**Example 2**

```
Input: nums = [-1,0]
Output: [-1,0]
```

**Example 3**

```
Input: nums = [0,1]
Output: [1,0]
```

## Constraints

- `2 <= nums.length <= 3 * 10^4`
- `-2^31 <= nums[i] <= 2^31 - 1`
- Every value in `nums` appears twice, except two values that appear once.

## Target complexity

O(n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

Combine all the numbers the way you did in Single Number. What do you get, and what does it tell you
about the two values you are looking for?

</details>

<details><summary>Hint 2</summary>

That result is not zero, because the two values are different. Pick one bit where they differ. How
can that bit split the whole array into two groups?

</details>

<details><summary>Hint 3</summary>

Check your idea with negative values and with `-2^31`.

</details>
