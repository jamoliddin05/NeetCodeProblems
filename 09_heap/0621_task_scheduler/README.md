# 621. Task Scheduler

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/task-scheduler/

## Task

You get a list of CPU `tasks`, each one labeled with a letter from `A` to `Z`, and a number `n`.
In each CPU interval the CPU either completes one task or stays idle. Tasks can be done in any
order, with one rule: between two tasks with the same label there must be a gap of **at least**
`n` intervals.

Return the **minimum** number of CPU intervals needed to complete all tasks.

## Examples

**Example 1**

```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
```

A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to
task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you
can do A again as 2 intervals have passed.

**Example 2**

```
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
```

A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

**Example 3**

```
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
```

A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This
leads to idling twice between repetitions of these tasks.

## Constraints

- `1 <= tasks.length <= 10^4`
- `tasks[i]` is an uppercase English letter.
- `0 <= n <= 100`

## Hints

<details><summary>Hint 1</summary>

Only how many times each letter appears matters, not where it appears in `tasks`.

</details>

<details><summary>Hint 2</summary>

Which label is the most likely to force the CPU to stay idle? What should happen to it early in the schedule?

</details>

<details><summary>Hint 3</summary>

When there are enough different labels to fill every gap, is any idle interval needed at all?

</details>
