# 257. Binary Tree Paths

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/binary-tree-paths/

## Task

You get the `root` of a binary tree. Return every path that goes from the root down to a leaf,
in any order.

A **leaf** is a node with no children. Each path is a string of the node values joined by `"->"`,
for example `"1->2->5"`.

## Examples

**Example 1**

```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

The tree:

```
    1
   / \
  2   3
   \
    5
```

**Example 2**

```
Input: root = [1]
Output: ["1"]
```

## Constraints

- The number of nodes in the tree is in the range `[1, 100]`.
- `-100 <= Node.val <= 100`

## Hints

<details><summary>Hint 1</summary>

A node with only one child is not a leaf. Where does a path have to stop?

</details>

<details><summary>Hint 2</summary>

While you walk down from the root, what do you need to carry along so that, at a leaf, the whole path is known?

</details>

<details><summary>Hint 3</summary>

After you finish with one child, the path for the other child must not contain anything from the first one.

</details>
