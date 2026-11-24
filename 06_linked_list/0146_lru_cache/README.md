# 146. LRU Cache

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/lru-cache/

## Task

Build a class `LRUCache`: a key-value store with a fixed capacity that, when full, throws out the
key that was used least recently. It has:

- `LRUCache(capacity)` creates an empty cache that holds at most `capacity` keys.
- `get(key)` returns the value stored for `key`, or `-1` if the key is not in the cache.
- `put(key, value)` stores `value` for `key`, replacing the old value if the key is already
  there. If adding a new key makes the cache hold more than `capacity` keys, remove the least
  recently used key.

Both `get` and `put` count as a use of the key. Each of them must run in O(1) average time.

## Example

**Example 1**

```
Input: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
       [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
```

```
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // returns 1
lRUCache.put(3, 3); // key 2 is the least recently used, so it is removed; cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // key 1 is the least recently used, so it is removed; cache is {4=4, 3=3}
lRUCache.get(1);    // returns -1 (not found)
lRUCache.get(3);    // returns 3
lRUCache.get(4);    // returns 4
```

## Constraints

- `1 <= capacity <= 3000`
- `0 <= key <= 10^4`
- `0 <= value <= 10^5`
- At most `2 * 10^5` calls in total to `get` and `put`.

## Target complexity

O(1) average time for each `get` and `put`, O(capacity) space.

## Hints

<details><summary>Hint 1</summary>

A dictionary finds a key in O(1), but it doesn't tell you which key was used least recently.

</details>

<details><summary>Hint 2</summary>

You need an order of the keys in which moving any key to the most recent end, and removing the
oldest key, both take O(1). Which structure lets you take an element out of the middle in O(1),
if you already hold a reference to it?

</details>

<details><summary>Hint 3</summary>

`get` also counts as a use. `put` on a key that is already there updates it and never removes
another key.

</details>
