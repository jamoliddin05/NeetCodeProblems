# 881. Boats to Save People

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/boats-to-save-people/

## Task

You get an array `people`, where `people[i]` is the weight of person `i`, and an integer
`limit`. You have as many boats as you want. A boat carries one or two people, and the total
weight in it must be at most `limit`.

Return the smallest number of boats that carries everyone.

## Examples

**Example 1**

```
Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
```

**Example 2**

```
Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
```

**Example 3**

```
Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
```

## Constraints

- `1 <= people.length <= 5 * 10^4`
- `1 <= people[i] <= limit <= 3 * 10^4`

## Hints

<details><summary>Hint 1</summary>

Every boat that carries two people saves one boat. So the task is to make as many pairs as
possible, where each pair fits under `limit`.

</details>

<details><summary>Hint 2</summary>

Think about the heaviest person. Who is the best partner for them, if anyone fits at all?

</details>

<details><summary>Hint 3</summary>

Pairing people who are next to each other by weight looks natural but fails on
`people = [1, 2, 2, 3], limit = 4`.

</details>
