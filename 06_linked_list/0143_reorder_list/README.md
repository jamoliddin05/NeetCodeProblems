# 143. Reorder List

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/reorder-list/

## Task

You get the `head` of a singly linked list `L0 → L1 → … → Ln-1 → Ln`. Rearrange it into

`L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …`

taking nodes from the front and from the back in turn. Change the links between the nodes, not
the values stored in them. The method returns nothing: it changes the list that `head` starts.

## Examples

**Example 1**

```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

**Example 2**

```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Constraints

- The number of nodes in the list is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 1000`

## Target complexity

O(n) time and O(1) extra space, where n is the number of nodes.

## Hints

<details><summary>Hint 1</summary>

Nodes are taken from the front and from the back in turn. In a singly linked list, moving
backwards is the hard part.

</details>

<details><summary>Hint 2</summary>

Look at the second half of the list on its own. In which order are its nodes used in the result?

</details>

<details><summary>Hint 3</summary>

The task can be split into smaller linked list tasks that you may already know how to solve.

</details>
