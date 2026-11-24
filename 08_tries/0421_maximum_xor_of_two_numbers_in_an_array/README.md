# 421. Maximum XOR of Two Numbers in an Array

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

## Task

You get an integer array `nums`. Pick two indices `i` and `j` with `0 <= i <= j < n` and compute
`nums[i] XOR nums[j]`. Return the largest result you can get.

Because `i` may equal `j`, an array with one number gives 0.

## Examples

**Example 1**

```
Input: nums = [3,10,5,25,2,8]
Output: 28
```

The maximum result is 5 XOR 25 = 28.

**Example 2**

```
Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
```

## Constraints

- `1 <= nums.length <= 2 * 10^5`
- `0 <= nums[i] <= 2^31 - 1`

## Target complexity

O(n · B) time, where n is the length of `nums` and B = 31 is the number of bits in a value.

## Hints

<details><summary>Hint 1</summary>

Trying every pair is about 2 × 10^10 XORs for the largest input, which is far too slow.

</details>

<details><summary>Hint 2</summary>

A result with a 1 in a higher bit is larger than any result with a 0 there, whatever the lower bits
are.

</details>

<details><summary>Hint 3</summary>

For one number, which other number would make its XOR largest? What would that number need to have
in its highest bit, then in the next bit, and so on?

</details>
