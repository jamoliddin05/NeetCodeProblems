# 102. Binary Tree Level Order Traversal

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/binary-tree-level-order-traversal/

## Task

You get the `root` of a binary tree. Return the values of its nodes grouped by level: one list for
the root, one list for the nodes one step below it, and so on. Inside each list the values go from
left to right.

An empty tree gives an empty list.

## Examples

**Example 1**

```
    3
   / \
  9  20
     / \
    15  7
```

```
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Example 2**

```
Input: root = [1]
Output: [[1]]
```

**Example 3**

```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 2000]`.
- `-1000 <= Node.val <= 1000`

## Target complexity

O(n) time and O(n) space, where n is the number of nodes.

## Hints

<details><summary>Hint 1</summary>

Suppose you already hold all nodes of one level, in order from left to right. How do you get all
nodes of the next level, also in order?

</details>

<details><summary>Hint 2</summary>

If you keep the nodes of several levels in one collection, how do you know where one level ends and
the next one begins?

</details>

<details><summary>Hint 3</summary>

A level can contain nodes from both the left and the right subtree of the root. Their order must
still be left to right across the whole tree.

</details>
