# 105. Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

## Task

You get two integer arrays that describe the same binary tree:

- `preorder` lists the values in preorder: a node, then its left subtree, then its right subtree;
- `inorder` lists the values in inorder: the left subtree, then the node, then the right subtree.

All values are different. Build that tree and return its root.

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
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Example 2**

```
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

## Constraints

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of unique values.
- Each value of `inorder` also appears in `preorder`.
- `preorder` is guaranteed to be the preorder traversal of the tree.
- `inorder` is guaranteed to be the inorder traversal of the tree.

## Target complexity

O(n) time and O(n) space, where n is the number of nodes.

## Hints

<details><summary>Hint 1</summary>

Which value of `preorder` is certainly the root of the whole tree?

</details>

<details><summary>Hint 2</summary>

Once you know the root, what does its position in `inorder` tell you about the left and the right
subtree? How many values does each of them have?

</details>

<details><summary>Hint 3</summary>

Searching `inorder` for a value again and again costs O(n) each time, which adds up on a long
chain. Can you find a value's position faster?

</details>
