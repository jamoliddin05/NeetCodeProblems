# 138. Copy List with Random Pointer

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/copy-list-with-random-pointer/

## Task

You get the `head` of a linked list of `n` nodes. Besides `next`, every node has a `random`
pointer that points to any node of the list or is `None`.

Build a deep copy: `n` brand-new nodes with the same values, where the `next` and `random`
pointers of the copies point to the matching copies. If original node X has `X.random -> Y`,
then its copy x must have `x.random -> y`, the copy of Y. No pointer in the copy may point to a
node of the original list. Return the head of the copy.

In the examples (and in `inputs.txt`) a list is written as `[[val, random_index], ...]`, where
`random_index` is the position (0 to n - 1) of the node that `random` points to, or `null`. Your
function only gets the head node.

## Examples

**Example 1**

```
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
```

**Example 2**

```
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
```

**Example 3**

```
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
```

## Constraints

- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `Node.random` is `null` or is pointing to some node in the linked list.

## Target complexity

O(n) time, where n is the number of nodes.

## Hints

<details><summary>Hint 1</summary>

Copying the values and the `next` pointers is the easy part. A `random` pointer can lead to a
node you haven't copied yet.

</details>

<details><summary>Hint 2</summary>

For any original node, you need a fast way to find its copy. Values can repeat, so a value is
not enough to tell nodes apart.

</details>

<details><summary>Hint 3</summary>

Think of two passes over the list. What can the first pass prepare so that the second pass can
set every pointer?

</details>
