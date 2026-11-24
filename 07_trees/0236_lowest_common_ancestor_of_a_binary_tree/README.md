# 236. Lowest Common Ancestor of a Binary Tree

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

## Task

You get the `root` of a binary tree and two of its nodes, `p` and `q`. Return their lowest common
ancestor: the deepest node that has both `p` and `q` in its subtree.

A node counts as part of its own subtree, so if `p` lies below `q`, the answer is `q` itself.

The tree is a plain binary tree, not a search tree: the values are in no particular order.

In `inputs.txt`, `p`, `q` and `expected` are written as node values; the tests pass your method the
nodes that hold `p` and `q`, and compare the value of the node you return.

## Examples

```
        3
      /   \
     5     1
    / \   / \
   6   2 0   8
      / \
     7   4
```

**Example 1**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
```

The LCA of nodes 5 and 1 is 3.

**Example 2**

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
```

The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA
definition.

**Example 3**

```
Input: root = [1,2], p = 1, q = 2
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range `[2, 10^5]`.
- `-10^9 <= Node.val <= 10^9`
- All `Node.val` are unique.
- `p != q`
- `p` and `q` will exist in the tree.

## Target complexity

O(n) time, where n is the number of nodes, and O(h) extra space, where h is the height of the tree.

## Hints

<details><summary>Hint 1</summary>

If `p` is in the left subtree of a node and `q` is in its right subtree, what can you say about that
node?

</details>

<details><summary>Hint 2</summary>

What should a subtree report to the node above it? Think about three situations: the subtree holds
neither node, exactly one of them, or both.

</details>

<details><summary>Hint 3</summary>

When you reach `p` before seeing `q`, can the answer be somewhere below `p`?

</details>
