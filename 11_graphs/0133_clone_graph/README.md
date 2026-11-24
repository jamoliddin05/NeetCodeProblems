# 133. Clone Graph

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/clone-graph/

## Task

You get a reference to one node of a connected undirected graph. Return a deep copy of the whole
graph: a new node for every original node, linked to each other the same way the originals are.
None of the returned nodes may be an original node.

Each node has an integer `val` and a list `neighbors` of the nodes it is connected to:

```python
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
```

Return the copy of the node you were given.

**How the tests describe a graph.** Node values are `1, 2, 3, ...`, so the value of a node is also
its number. The graph is written as an adjacency list `adjList`, where `adjList[i]` lists the
values of the neighbours of the node with value `i + 1`. You always get the node with value `1`
(or `None` when the graph is empty). The expected output is the adjacency list of the copy.

## Examples

**Example 1**

```
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
```

There are 4 nodes. Node 1 is connected to nodes 2 and 4, node 2 to nodes 1 and 3, node 3 to
nodes 2 and 4, and node 4 to nodes 1 and 3.

**Example 2**

```
Input: adjList = [[]]
Output: [[]]
```

The graph has one node with value 1 and no neighbours.

**Example 3**

```
Input: adjList = []
Output: []
```

The graph is empty: there are no nodes.

## Constraints

- The number of nodes in the graph is in the range `[0, 100]`.
- `1 <= Node.val <= 100`
- `Node.val` is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The graph is connected, and all nodes can be reached from the given node.

## Target complexity

O(V + E) time and O(V) space, where V is the number of nodes and E is the number of edges.

## Hints

<details><summary>Hint 1</summary>

The graph can have cycles. While you are copying, how do you know whether a node already has a
copy?

</details>

<details><summary>Hint 2</summary>

When you copy a neighbour list, every entry must point to a copy, never to an original node. Each
original node must get exactly one copy, even when many nodes point to it.

</details>

<details><summary>Hint 3</summary>

Don't forget the empty graph: the input node can be `None`.

</details>
