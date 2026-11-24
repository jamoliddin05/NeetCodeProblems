# 543. Diameter of Binary Tree

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/diameter-of-binary-tree/

## Task

You get the `root` of a binary tree. Return its diameter: the number of edges on the longest path
between any two nodes of the tree.

The path does not have to go through the root. Its length is counted in edges, not in nodes, so a
tree with a single node has diameter 0.

## Examples

**Example 1**

```
      1
     / \
    2   3
   / \
  4   5
```

```
Input: root = [1,2,3,4,5]
Output: 3
```

3 is the length of the path [4,2,1,3] or [5,2,1,3].

**Example 2**

```
Input: root = [1,2]
Output: 1
```

## Constraints

- The number of nodes in the tree is in the range `[1, 10^4]`.
- `-100 <= Node.val <= 100`

## Target complexity

O(n) time, where n is the number of nodes, and O(h) extra space, where h is the height of the tree.

## Hints

<details><summary>Hint 1</summary>

Every path has one highest node, where it stops going up and starts going down. What do the two
halves of the path look like, seen from that node?

</details>

<details><summary>Hint 2</summary>

For one fixed node, how long is the longest path whose highest node is that node? What would you
need to know about its left and right subtrees to answer that?

</details>

<details><summary>Hint 3</summary>

The best path can sit entirely inside one subtree, so the answer at the root alone is not enough.

</details>
