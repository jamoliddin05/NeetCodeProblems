# 31. Next Permutation

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/next-permutation/

## Task

You get an integer array `nums`. Think of all the ways to arrange its values, sorted from
smallest to largest the way words are sorted in a dictionary (compare the first values, then
the second, and so on). Change `nums` into the arrangement that comes right after the current
one in that order.

If `nums` is already the largest arrangement, change it into the smallest one, which is the
values in ascending order.

For example:

- The next permutation of `[1, 2, 3]` is `[1, 3, 2]`.
- The next permutation of `[2, 3, 1]` is `[3, 1, 2]`.
- The next permutation of `[3, 2, 1]` is `[1, 2, 3]`, because no larger arrangement exists.

Change `nums` in place and use only constant extra memory. The method returns nothing.

## Examples

**Example 1**

```
Input: nums = [1,2,3]
Output: [1,3,2]
```

**Example 2**

```
Input: nums = [3,2,1]
Output: [1,2,3]
```

**Example 3**

```
Input: nums = [1,1,5]
Output: [1,5,1]
```

## Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 100`

## Target complexity

O(1) extra space: the statement asks for an in-place change with constant extra memory.

## Hints

<details><summary>Hint 1</summary>

Listing every arrangement is far too slow: 100 values have about `10^158` arrangements. The
answer has to come from looking at `nums` itself.

</details>

<details><summary>Hint 2</summary>

To get the very next arrangement, you want to change as little as possible at the front. Look
at the array from the right end. When can a tail of the array not be made any larger?

</details>

<details><summary>Hint 3</summary>

Write out all six arrangements of `[1, 2, 3]` in order and compare each one with the next. Which
positions changed each time, and how does the changed tail look?

</details>
