# 210. Course Schedule II

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/course-schedule-ii/

## Task

There are `numCourses` courses, numbered from `0` to `numCourses - 1`. You get a list
`prerequisites`, where `prerequisites[i] = [a, b]` means you must finish course `b` before you
can take course `a`.

Return an order in which you can take all the courses. If there are several valid orders, return
any one of them. If it is impossible to finish all the courses, return an empty list.

For example, the pair `[0, 1]` means that course `1` must be finished before course `0`.

## Examples

**Example 1**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
```

Course 0 must come before course 1, so the only valid order is `[0,1]`.

**Example 2**

```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
```

Course 3 needs courses 1 and 2, and both of them need course 0. Both `[0,1,2,3]` and `[0,2,1,3]`
are valid answers.

**Example 3**

```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`
- `prerequisites[i].length == 2`
- `0 <= a, b < numCourses`
- `a != b`
- All the pairs `[a, b]` are distinct.

## Target complexity

O(V + E) time and O(V + E) space, where V is `numCourses` and E is the length of
`prerequisites`.

## Hints

<details><summary>Hint 1</summary>

Which courses can go first in the order? What changes for the other courses once those are taken?

</details>

<details><summary>Hint 2</summary>

If your order stops growing before it contains every course, what does that tell you about the
prerequisites?

</details>

<details><summary>Hint 3</summary>

Courses that appear in no pair at all still have to be in the answer.

</details>
