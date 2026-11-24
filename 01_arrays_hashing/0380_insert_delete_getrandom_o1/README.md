# 380. Insert Delete GetRandom O(1)

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/insert-delete-getrandom-o1/

## Task

Build a class `RandomizedSet` that holds a set of integers (no value twice). It has:

- `RandomizedSet()` creates an empty set.
- `insert(val)` adds `val` if it is not in the set yet. Returns `true` if it was added, `false`
  if it was already there.
- `remove(val)` deletes `val` if it is in the set. Returns `true` if it was deleted, `false` if
  it was not there.
- `getRandom()` returns one element of the set, picked at random. Every element must have the
  same chance of being picked. The set is never empty when this is called.

Each of these must run in O(1) time on average.

## Example

**Example 1**

```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]
```

```
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
```

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- At most `2 * 10^5` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be at least one element in the data structure when `getRandom` is called.

## Target complexity

Average O(1) time for each call, O(n) space, where n is the number of elements in the set.

## Hints

<details><summary>Hint 1</summary>

A Python `set` gives O(1) insert and remove. Why can't it give an O(1) `getRandom`?

</details>

<details><summary>Hint 2</summary>

Picking a random element is easy and O(1) in one kind of structure. Which one, and what is slow
in it?

</details>

<details><summary>Hint 3</summary>

Deleting from the middle of that structure is the slow part. Deleting from one particular
place in it is not. Does the order of elements matter here?

</details>
