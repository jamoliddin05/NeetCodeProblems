# 860. Lemonade Change

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/lemonade-change/

## Task

You sell lemonade for $5 a cup. Customers stand in a line and come to you one at a time, in the
order given by the array `bills`. Each customer buys exactly one cup and pays with one bill:
$5, $10 or $20. You must give each customer the right change, so that every customer pays
exactly $5 in the end.

You start with no money at all, so the only bills you can give back are bills that earlier
customers paid you.

Return `true` if you can give every customer the right change, `false` otherwise.

## Examples

**Example 1**

```
Input: bills = [5,5,5,10,20]
Output: true
```

The first three customers pay with $5 bills. The fourth pays $10 and gets one $5 back. The fifth
pays $20 and gets one $10 and one $5 back.

**Example 2**

```
Input: bills = [5,5,10,10,20]
Output: false
```

When the last customer pays $20, you hold only two $10 bills, so you can't give back exactly $15.

## Constraints

- `1 <= bills.length <= 10^5`
- `bills[i]` is `5`, `10` or `20`.

## Target complexity

O(n) time and O(1) extra space, where n is the length of `bills`.

## Hints

<details><summary>Hint 1</summary>

You never need to know in which order you got your bills, only how many of each kind you hold.
Which kinds of bills can you ever give back as change?

</details>

<details><summary>Hint 2</summary>

A $20 bill needs $15 back, and sometimes there is more than one way to make $15. Does your choice
matter for the customers who come later?

</details>
