# 1004. Max Consecutive Ones III

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/max-consecutive-ones-iii/

## Task

You get an array `nums` that holds only `0`s and `1`s, and an integer `k`.
You may turn at most `k` of the `0`s into `1`s.

Return the length of the longest block of `1`s standing next to each other that you can get this way.

## Examples

**Example 1**

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
```

Turn the zeros at indexes 5 and 10 into ones: [1,1,1,0,0,1,1,1,1,1,1].
The longest block of ones is then indexes 5 to 10.

**Example 2**

```
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
```

Turn the zeros at indexes 4, 5 and 9 into ones: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1].
The longest block of ones is then indexes 2 to 11.

## Constraints

- `1 <= nums.length <= 10^5`
- `nums[i]` is either `0` or `1`.
- `0 <= k <= nums.length`

## Target complexity

O(n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

You don't have to change the array. Look at one block of `nums`: can it become all ones with at most `k` changes? What single number about the block decides that?

</details>

<details><summary>Hint 2</summary>

Checking every block is O(n^2). If a block can become all ones, can every shorter block inside it too?

</details>

<details><summary>Hint 3</summary>

Try `k = 0` and a `k` larger than the number of zeros on your idea.

</details>
