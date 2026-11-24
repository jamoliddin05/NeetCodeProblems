# 206. Reverse Linked List

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/reverse-linked-list/

## Task

You get the `head` of a singly linked list. Reverse the list so that the last node comes first,
and return the new head. An empty list is `None`.

Follow-up: a linked list can be reversed both iteratively and recursively. Can you write both?

## Examples

**Example 1**

```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2**

```
Input: head = [1,2]
Output: [2,1]
```

**Example 3**

```
Input: head = []
Output: []
```

## Constraints

- The number of nodes in the list is in the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

## Target complexity

O(n) time, where n is the number of nodes. The iterative version needs only O(1) extra space.

## Hints

<details><summary>Hint 1</summary>

In the reversed list, each node's `next` must point to the node that came before it. When you
change a node's `next`, what do you need to remember first so you don't lose the rest of the list?

</details>

<details><summary>Hint 2</summary>

Draw three nodes on paper and change one arrow at a time.

</details>

<details><summary>Hint 3</summary>

For the recursive version: if the part of the list after `head` were already reversed, what
would you still need to fix?

</details>
