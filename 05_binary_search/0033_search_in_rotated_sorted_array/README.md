# 33. Search in Rotated Sorted Array

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/search-in-rotated-sorted-array/

## Task

An array of distinct integers was sorted in ascending order and then possibly rotated: an
unknown number `k` of elements was taken from the front and moved to the back, keeping their
order. For example, `[0,1,2,4,5,6,7]` rotated by 3 becomes `[4,5,6,7,0,1,2]`.

You get the array `nums` after the possible rotation and an integer `target`. Return the index
of `target` in `nums`, or `-1` if it is not there.

Your algorithm must run in O(log n) time.

## Examples

**Example 1**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Example 3**

```
Input: nums = [1], target = 0
Output: -1
```

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are unique.
- `nums` is an ascending array that is possibly rotated.
- `-10^4 <= target <= 10^4`

## Target complexity

O(log n) time and O(1) extra space, where n is the length of `nums`.

## Hints

<details><summary>Hint 1</summary>

Split the array at any index. At least one of the two parts is sorted in the normal way. How can
you tell which one by looking only at the values at its ends?

</details>

<details><summary>Hint 2</summary>

For a part that is sorted, you can tell with two comparisons whether `target` can be inside it.

</details>

<details><summary>Hint 3</summary>

Test the boundaries of your loop on a two-element array such as `[3, 1]`.

</details>
