# 1971. Find if Path Exists in Graph

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/find-if-path-exists-in-graph/

## Task

There is an undirected graph with `n` vertices numbered from `0` to `n - 1`. You get its edges as
a list `edges`, where `edges[i] = [u, v]` is an edge between `u` and `v` that can be used in
both directions. Two vertices have at most one edge between them, and no vertex has an edge to
itself.

Return `true` if there is a path from vertex `source` to vertex `destination`, and `false`
otherwise.

## Examples

**Example 1**

```
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
```

There are two paths from vertex 0 to vertex 2: `0 -> 1 -> 2` and `0 -> 2`.

**Example 2**

```
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
```

Vertex 0 is only connected to vertices 1 and 2, so there is no path to vertex 5.

## Constraints

- `1 <= n <= 2 * 10^5`
- `0 <= edges.length <= 2 * 10^5`
- `edges[i].length == 2`
- `0 <= u, v <= n - 1`
- `u != v`
- `0 <= source, destination <= n - 1`
- There are no duplicate edges.
- There are no self edges.

## Target complexity

O(n + E) time and O(n + E) space, where E is the length of `edges`.

## Hints

<details><summary>Hint 1</summary>

The edges come as a flat list. What form of the graph lets you quickly list the neighbours of one
vertex?

</details>

<details><summary>Hint 2</summary>

The graph can have cycles. How do you avoid visiting the same vertex over and over?

</details>

<details><summary>Hint 3</summary>

What should you return when `source` and `destination` are the same vertex?

</details>
