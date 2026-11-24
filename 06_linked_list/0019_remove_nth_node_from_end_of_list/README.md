# 19. Remove Nth Node From End of List

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Task

You get the `head` of a linked list and an integer `n`. Remove the `n`-th node counting from the
end of the list (`n = 1` is the last node) and return the head of the changed list.

Follow-up: can you do it in one pass over the list?

## Examples

**Example 1**

```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```

**Example 2**

```
Input: head = [1], n = 1
Output: []
```

**Example 3**

```
Input: head = [1,2], n = 1
Output: [1]
```

## Constraints

- The number of nodes in the list is `sz`.
- `1 <= sz <= 30`
- `0 <= Node.val <= 100`
- `1 <= n <= sz`

## Target complexity

O(sz) time and O(1) extra space; one pass for the follow-up.

## Hints

<details><summary>Hint 1</summary>

To remove a node, you change the `next` of the node before it. What happens when the node to
remove is the head, which has no node before it?

</details>

<details><summary>Hint 2</summary>

An extra node placed in front of the head gives every real node a node before it.

</details>

<details><summary>Hint 3</summary>

For one pass: when one pointer reaches the end of the list, where is a second pointer that has
always stayed a fixed number of nodes behind it?

</details>
