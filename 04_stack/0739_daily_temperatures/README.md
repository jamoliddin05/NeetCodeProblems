# 739. Daily Temperatures

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/daily-temperatures/

## Task

You get an array `temperatures`, where `temperatures[i]` is the temperature on day `i`.
Return an array `answer` of the same length, where `answer[i]` is how many days after day `i`
you have to wait for a strictly warmer day. If no later day is warmer, `answer[i]` is `0`.

## Examples

**Example 1**

```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Example 2**

```
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
```

**Example 3**

```
Input: temperatures = [30,60,90]
Output: [1,1,0]
```

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`

## Target complexity

O(n) time and O(n) space, where n is the length of `temperatures`.

## Hints

<details><summary>Hint 1</summary>

Scanning forward from every day is O(n^2), which is too slow when many days wait a long time. Turn the question around: when you reach a warm day, which earlier days does it answer?

</details>

<details><summary>Hint 2</summary>

Think about the days that are still waiting for a warmer day. What can you say about their temperatures, in the order the days came?

</details>

<details><summary>Hint 3</summary>

An equal temperature is not warmer. Try `[70, 70, 71]`.

</details>
