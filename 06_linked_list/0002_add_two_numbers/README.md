# 2. Add Two Numbers

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/add-two-numbers/

## Task

You get two non-empty linked lists `l1` and `l2`. Each one is a non-negative integer written one
digit per node, with the lowest digit first: `[2,4,3]` is the number 342. Add the two numbers and
return the sum as a linked list in the same form.

Neither number has leading zeros, except the number 0 itself.

## Examples

**Example 1**

```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
```

342 + 465 = 807.

**Example 2**

```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3**

```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
```

9999999 + 9999 = 10009998.

## Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Target complexity

O(max(m, n)) time, where m and n are the lengths of the two lists.

## Hints

<details><summary>Hint 1</summary>

The lowest digit comes first. That is the same order in which you add numbers on paper, from
right to left.

</details>

<details><summary>Hint 2</summary>

The lists can have different lengths. What do you add when one of them has run out?

</details>

<details><summary>Hint 3</summary>

After both lists have run out, there can still be one more digit to write.

</details>
