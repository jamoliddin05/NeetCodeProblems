# 155. Min Stack

**Difficulty:** Medium
**NeetCode:** https://neetcode.io/problems/minimum-stack/question?list=neetcode150
**LeetCode:** https://leetcode.com/problems/min-stack/

## Task

Build a class `MinStack` that works like a normal stack and can also tell you its smallest element.
It has:

- `MinStack()` creates an empty stack.
- `push(val)` puts the integer `val` on top.
- `pop()` removes the top element.
- `top()` returns the top element.
- `getMin()` returns the smallest element currently in the stack.

Each of these must run in O(1) time.

## Example

**Example 1**

```
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
Output: [null, null, null, null, 0, null, 2, 1]
```

```
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // returns 0
minStack.pop();
minStack.top();    // returns 2
minStack.getMin(); // returns 1
```

## Constraints

- `-2^31 <= val <= 2^31 - 1`
- `pop`, `top` and `getMin` are only called when the stack is not empty.
- At most `3 * 10^4` calls in total to `push`, `pop`, `top` and `getMin`.

## Target complexity

O(1) time for each call, O(n) space, where n is the largest number of elements the stack holds.

## Hints

<details><summary>Hint 1</summary>

Scanning the whole stack in `getMin` is O(n). The answer has to be ready before `getMin` is called.

</details>

<details><summary>Hint 2</summary>

When you push an element, what is the minimum of the stack from the bottom up to that element? Does it ever change while that element stays in the stack?

</details>

<details><summary>Hint 3</summary>

After a `pop`, the minimum must be what it was before that element was pushed.

</details>
