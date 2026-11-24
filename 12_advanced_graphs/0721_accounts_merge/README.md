# 721. Accounts Merge

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/accounts-merge/

## Task

You get a list `accounts`. Each account is a list of strings: `accounts[i][0]` is a name, and the
rest of the strings are emails of that account.

Two accounts belong to the same person if they have at least one email in common. This also links
accounts through others: if account A shares an email with B, and B shares one with C, then A, B
and C all belong to one person. Two accounts with the same name do not have to belong to the same
person, but all accounts of one person have the same name.

Merge the accounts of each person into one account and return the list of merged accounts. In
each merged account, the first element is the name and the rest are all of that person's emails,
each listed once and sorted. The accounts themselves can be returned in any order.

## Examples

**Example 1**

```
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
```

The first and second accounts share `"johnsmith@mail.com"`, so they belong to the same John. The
third John and Mary share no email with anyone, so they stay separate. The answer
`[["Mary","mary@mail.com"],["John","johnnybravo@mail.com"],["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"]]`
is also accepted.

**Example 2**

```
Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
```

## Constraints

- `1 <= accounts.length <= 1000`
- `2 <= accounts[i].length <= 10`
- `1 <= accounts[i][j].length <= 30`
- `accounts[i][0]` consists of English letters.
- `accounts[i][j]` (for `j > 0`) is a valid email.

## Target complexity

O(N log N) time and O(N) space, where N is the total number of emails in all accounts.

## Hints

<details><summary>Hint 1</summary>

An email that appears in two accounts joins them. Which accounts are joined only through a chain
of other accounts?

</details>

<details><summary>Hint 2</summary>

The order of the accounts in the input does not matter. Two accounts can turn out to belong
together only after you have read a third account listed later.

</details>

<details><summary>Hint 3</summary>

Emails are sorted as plain strings, by character codes: digits come before capital letters, and
capital letters come before `_` and small letters.

</details>
