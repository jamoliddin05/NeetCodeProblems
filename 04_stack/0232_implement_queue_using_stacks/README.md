# 232. Implement Queue using Stacks

**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/implement-queue-using-stacks/

## Task

Build a class `MyQueue` that works as a first in, first out (FIFO) queue, using only two stacks
to hold the elements. It has:

- `MyQueue()` creates an empty queue.
- `push(x)` adds the integer `x` to the back of the queue.
- `pop()` removes the element at the front of the queue and returns it.
- `peek()` returns the element at the front of the queue without removing it.
- `empty()` returns `true` if the queue has no elements, `false` otherwise.

Rules for the stacks:

- Use only the standard stack operations: push to the top, look at or pop from the top, get the
  size, and check if it is empty.
- In Python a list works as a stack (`append`, `pop()`, `[-1]`, `len`), as long as you use only
  those operations. Reading from the front of the list or `pop(0)` is not allowed.

## Example

**Example 1**

```
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
```

```
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek();  // return 1
myQueue.pop();   // return 1, queue is [2]
myQueue.empty(); // return false
```

## Constraints

- `1 <= x <= 9`
- At most `100` calls will be made to `push`, `pop`, `peek` and `empty`.
- All the calls to `pop` and `peek` are valid (the queue is not empty).

## Target complexity

Follow-up from LeetCode: make each operation amortized O(1) time. That means `n` operations
take O(n) time in total, even if one single operation sometimes takes longer.

## Hints

<details><summary>Hint 1</summary>

Push 1, 2, 3 onto a stack, then pop them one by one. In what order do they come out? What happens to the order when the elements pass through a stack twice?

</details>

<details><summary>Hint 2</summary>

Moving all elements between the stacks on every call is O(n) per call. When is moving them really needed?

</details>

<details><summary>Hint 3</summary>

Check your idea on pushes that come between pops: push 1, push 2, pop, push 3, pop, pop.

</details>
