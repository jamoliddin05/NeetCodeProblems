# 98. Validate Binary Search Tree

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/validate-binary-search-tree/

## Task

You get the `root` of a binary tree. Return `true` if it is a valid binary search tree (BST),
`false` otherwise.

The tree is a valid BST when, for every node:

1. every value in its left subtree is strictly less than the node's value;
2. every value in its right subtree is strictly greater than the node's value;
3. both of its subtrees are valid BSTs too.

Equal values are not allowed anywhere in the order.

## Examples

**Example 1**

```
  2
 / \
1   3
```

```
Input: root = [2,1,3]
Output: true
```

**Example 2**

```
  5
 / \
1   4
   / \
  3   6
```

```
Input: root = [5,1,4,null,null,3,6]
Output: false
```

The root node's value is 5 but its right child's value is 4.

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-2^31 <= Node.val <= 2^31 - 1`

## Target complexity

O(n) time, where n is the number of nodes, and O(h) extra space, where h is the height of the tree.

## Hints

<details><summary>Hint 1</summary>

Comparing each node only with its own children is not enough. In `[5,4,6,null,null,3,7]` every
parent and child are in the right order, but 3 sits in the right subtree of 5.

</details>

<details><summary>Hint 2</summary>

Every node must fit between a lowest and a highest allowed value, set by the nodes above it. How do
those two limits change when you step to a left child, and when you step to a right child?

</details>

<details><summary>Hint 3</summary>

Node values can be exactly `-2^31` or `2^31 - 1`. Make sure the limits you start with don't reject
them.

</details>
