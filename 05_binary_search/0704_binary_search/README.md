# 704. Binary Search

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/binary-search/

## Task

You get an array of integers `nums` sorted in ascending order, with no repeated values, and an
integer `target`. Return the index of `target` in `nums`, or `-1` if it is not there.

Your algorithm must run in O(log n) time.

## Examples

**Example 1**

```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
```

9 is in `nums` at index 4.

**Example 2**

```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
```

2 is not in `nums`, so the answer is -1.

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All the integers in `nums` are unique.
- `nums` is sorted in ascending order.

## Target complexity

O(log n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

Compare `target` with one element in the middle of the array. Because the array is sorted, what
does that one comparison tell you about all the elements on one side of it?

</details>

<details><summary>Hint 2</summary>

Keep two indexes that mark the part of the array where `target` can still be. When is that part
empty?

</details>

<details><summary>Hint 3</summary>

Try your loop by hand on arrays of one and two elements. Does it stop, and does it look at every
index it should?

</details>
