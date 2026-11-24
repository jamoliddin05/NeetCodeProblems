# 1046. Last Stone Weight

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/last-stone-weight/

## Task

You get an array `stones` where `stones[i]` is the weight of the `i`-th stone.

The game goes in turns. On each turn, take the two heaviest stones, with weights `x <= y`, and
smash them together:

- if `x == y`, both stones are destroyed;
- if `x != y`, the stone of weight `x` is destroyed and the other one now weighs `y - x`.

The game ends when at most one stone is left. Return the weight of that stone, or `0` if no
stones are left.

## Examples

**Example 1**

```
Input: stones = [2,7,4,1,8,1]
Output: 1
```

We combine 7 and 8 to get 1, so the array becomes [2,4,1,1,1]. Then we combine 2 and 4 to get 2,
so the array becomes [2,1,1,1]. Then we combine 2 and 1 to get 1, so the array becomes [1,1,1].
Then we combine 1 and 1 to get 0, so the array becomes [1], and that is the weight of the last
stone.

**Example 2**

```
Input: stones = [1]
Output: 1
```

## Constraints

- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`

## Hints

<details><summary>Hint 1</summary>

The order of the turns is fixed by the rules, so the answer comes from playing the game exactly as described.

</details>

<details><summary>Hint 2</summary>

After a smash, the leftover stone can be heavier than some of the others or lighter than all of them. Where does it go before the next turn?

</details>

<details><summary>Hint 3</summary>

Each turn needs only the two heaviest stones. Is there a way to keep the heaviest stone ready without sorting the whole list again every turn?

</details>
