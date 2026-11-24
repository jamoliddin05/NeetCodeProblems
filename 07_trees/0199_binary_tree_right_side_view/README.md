# 199. Binary Tree Right Side View

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/binary-tree-right-side-view/

## Task

You get the `root` of a binary tree. Picture yourself standing to the right of the tree and
looking at it. On each level you see only one node: the one furthest to the right on that level.
Return the values of the nodes you see, from the top level to the bottom one.

An empty tree gives an empty list.

## Examples

**Example 1**

```
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
```

```
    1      <- 1
   / \
  2   3    <- 3
   \   \
    5   4  <- 4
```

**Example 2**

```
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
```

```
      1    <- 1
     / \
    2   3  <- 3
   /
  4        <- 4
 /
5          <- 5
```

**Example 3**

```
Input: root = [1,null,3]
Output: [1,3]
```

**Example 4**

```
Input: root = []
Output: []
```

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`.
- `-100 <= Node.val <= 100`

## Target complexity

O(n) time and O(n) space, where n is the number of nodes.

## Hints

<details><summary>Hint 1</summary>

Always following the right child is not enough: look at Example 2, where the nodes 4 and 5 are in
the left subtree.

</details>

<details><summary>Hint 2</summary>

The answer has one value per level. If you go through the nodes of one level in some fixed order,
which of them do you keep?

</details>

<details><summary>Hint 3</summary>

How do you know that you are seeing a level for the first time?

</details>
