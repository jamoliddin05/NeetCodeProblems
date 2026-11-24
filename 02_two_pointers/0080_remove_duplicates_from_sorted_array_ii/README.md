# 80. Remove Duplicates from Sorted Array II

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

## Task

You get an integer array `nums` sorted in non-decreasing order. Remove extra copies so that each
value appears at most twice, and keep the values in their original order.

Do it in place: put the result into the first `k` positions of `nums` and return `k`. What is
left in `nums` after position `k` does not matter. Don't create another array; use only O(1)
extra memory.

The site checks your answer like this:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

## Examples

**Example 1**

```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2**

```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in non-decreasing order.

## Target complexity

O(1) extra space: the statement asks for an in-place change with constant extra memory.

## Hints

<details><summary>Hint 1</summary>

Deleting an element from the middle of a Python list moves everything after it, so many
deletions get slow. The result only has to sit in the first `k` positions. Do you need to delete
anything at all?

</details>

<details><summary>Hint 2</summary>

When you read a value, what do you need to know about the result written so far to decide
whether this value may be added?

</details>

<details><summary>Hint 3</summary>

Check your rule on Example 1 step by step. Compare against what is already in the result, not
against what used to be in the input at that position.

</details>
