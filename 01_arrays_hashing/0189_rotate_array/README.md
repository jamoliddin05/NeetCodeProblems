# 189. Rotate Array

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/rotate-array/

## Task

You get an integer array `nums` and a non-negative integer `k`. Shift every element `k` places to
the right. An element pushed past the last position comes back in at the front.

Change `nums` in place. The method returns nothing.

## Examples

**Example 1**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2**

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

## Constraints

- `1 <= nums.length <= 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `0 <= k <= 10^5`

## Target complexity

Follow-up from the site: find as many solutions as you can (there are at least three), and try
one that works in place with O(1) extra space.

## Hints

<details><summary>Hint 1</summary>

Moving everything one step at a time, `k` times, is O(n * k): up to `10^10` steps here. Also,
`k` can be larger than the length of the array. Does a rotation by `k` ever differ from a
rotation by a smaller number?

</details>

<details><summary>Hint 2</summary>

With a second array the task is easy: for each index, where does its element end up?

</details>

<details><summary>Hint 3</summary>

Without a second array: compare Example 1 before and after on paper. The last `k` elements and
the first `n - k` elements each keep their own order; only the two blocks trade places. Which
operations can you do in place on an array or on a part of it?

</details>
