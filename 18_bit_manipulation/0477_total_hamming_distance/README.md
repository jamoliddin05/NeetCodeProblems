# 477. Total Hamming Distance

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/total-hamming-distance/

## Task

The Hamming distance between two integers is the number of bit positions where their bits are
different.

You get an integer array `nums`. Return the sum of the Hamming distances over all pairs of numbers
in `nums`.

## Examples

**Example 1**

```
Input: nums = [4,14,2]
Output: 6
```

In binary, 4 is 0100, 14 is 1110 and 2 is 0010 (only the four lowest bits are shown). The answer is
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.

**Example 2**

```
Input: nums = [4,14,4]
Output: 4
```

## Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^9`
- The answer fits in a 32-bit integer.

## Hints

<details><summary>Hint 1</summary>

With `10^4` numbers there are about `5 * 10^7` pairs. Checking every pair is too slow in Python.

</details>

<details><summary>Hint 2</summary>

Look at one bit position on its own. How much does that position add to the total?

</details>

<details><summary>Hint 3</summary>

At one bit position, which pairs add 1 to the total? Can you count them without listing them?

</details>
