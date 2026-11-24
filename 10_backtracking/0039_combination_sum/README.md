# 39. Combination Sum

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/combination-sum/

## Task

You get an array `candidates` of distinct integers and an integer `target`. Return every unique
combination of candidates whose numbers add up to `target`, in any order.

Each candidate may be used any number of times. Two combinations are different only if at
least one number is used a different number of times in them, so `[2,2,3]` and `[2,3,2]` count
as the same combination.

The test data guarantees that fewer than `150` combinations add up to `target`.

## Examples

**Example 1**

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used more than once. 7 is a
candidate, and 7 = 7. These are the only two combinations.

**Example 2**

```
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

**Example 3**

```
Input: candidates = [2], target = 1
Output: []
```

## Constraints

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**.
- `1 <= target <= 40`

## Hints

<details><summary>Hint 1</summary>

Picking 2 then 3 and picking 3 then 2 give the same combination. How can you make sure each combination is built in only one way?

</details>

<details><summary>Hint 2</summary>

After you choose a number, what is left to reach? When should you stop going further?

</details>

<details><summary>Hint 3</summary>

If you build a combination in a shared list that you change as you go, make sure that what you add to the answer is a copy.

</details>
