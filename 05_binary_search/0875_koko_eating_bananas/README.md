# 875. Koko Eating Bananas

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/koko-eating-bananas/

## Task

There are `n` piles of bananas; pile `i` has `piles[i]` bananas. Koko has `h` hours to eat all of
them.

She picks a whole-number eating speed `k` (bananas per hour). Every hour she chooses one pile and
eats `k` bananas from it. If that pile has fewer than `k` bananas left, she eats all of them and
does nothing else for the rest of that hour.

Return the smallest speed `k` that lets her eat every banana within `h` hours.

## Examples

**Example 1**

```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

At speed 4 the piles take 1, 2, 2 and 3 hours: 8 hours in total.

**Example 2**

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

There are 5 piles and 5 hours, so each pile must be eaten in one hour. The largest pile has 30
bananas.

**Example 3**

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

At speed 23 the first pile takes 2 hours and each of the others takes 1 hour: 6 hours in total.

## Constraints

- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`

## Target complexity

O(n log m) time and O(1) extra space, where n is the number of piles and m is the largest pile.

## Hints

<details><summary>Hint 1</summary>

If Koko can finish at speed `k`, she can also finish at every speed larger than `k`.

</details>

<details><summary>Hint 2</summary>

For one fixed speed, how many hours does a single pile take? Work it out with arithmetic, without
going hour by hour.

</details>

<details><summary>Hint 3</summary>

What is the smallest speed worth trying, and what speed is always fast enough? Trying every speed
between them one by one is too slow when the piles hold up to 10^9 bananas.

</details>
