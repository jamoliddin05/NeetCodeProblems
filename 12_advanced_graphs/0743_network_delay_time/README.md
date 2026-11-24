# 743. Network Delay Time

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/network-delay-time/

## Task

A network has `n` nodes numbered from `1` to `n`. You get a list `times`, where
`times[i] = [u, v, w]` is a one-way link: a signal sent from node `u` reaches node `v` after `w`
units of time.

A signal is sent from node `k`. Return the time it takes until every one of the `n` nodes has
received the signal. If some node can never receive it, return `-1`.

## Examples

**Example 1**

```
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

Node 2 reaches nodes 1 and 3 after 1 unit of time, and node 4 through node 3 after 2 units.

**Example 2**

```
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
```

**Example 3**

```
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
```

The only link goes from node 1 to node 2, so a signal from node 2 never reaches node 1.

## Constraints

- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`
- `times[i].length == 3`
- `1 <= u, v <= n`
- `u != v`
- `0 <= w <= 100`
- All the pairs `(u, v)` are unique (there are no repeated links).

## Target complexity

O(E log V) time and O(V + E) space, where V is `n` and E is the length of `times`.

## Hints

<details><summary>Hint 1</summary>

Each node receives the signal at the earliest moment some path from `k` delivers it. How does the
answer for the whole network follow from those moments?

</details>

<details><summary>Hint 2</summary>

The path with the fewest links is not always the fastest one. A node can first be reached late
and later be reached earlier through a different path.

</details>

<details><summary>Hint 3</summary>

The time for node `k` itself is certain from the start. Which node's time can you be certain of
next, and why can no other path improve it?

</details>
