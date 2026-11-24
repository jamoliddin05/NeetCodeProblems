# 207. Course Schedule

**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/course-schedule/

## Task

There are `numCourses` courses, numbered from `0` to `numCourses - 1`. You get a list
`prerequisites`, where `prerequisites[i] = [a, b]` means you must finish course `b` before you
can take course `a`.

Return `true` if it is possible to finish all the courses, and `false` otherwise.

For example, the pair `[0, 1]` means that course `1` must be finished before course `0`.

## Examples

**Example 1**

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
```

There are 2 courses. Course 0 must come before course 1, so you take course 0 and then course 1.

**Example 2**

```
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
```

Course 0 must come before course 1, and course 1 must come before course 0. Neither can be taken
first.

## Constraints

- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i].length == 2`
- `0 <= a, b < numCourses`
- All the pairs `prerequisites[i]` are unique.

## Target complexity

O(V + E) time and O(V + E) space, where V is `numCourses` and E is the length of
`prerequisites`.

## Hints

<details><summary>Hint 1</summary>

Draw each course as a point and each pair as an arrow. What shape of arrows makes it impossible to
finish?

</details>

<details><summary>Hint 2</summary>

A course with no unfinished prerequisites can be taken right away. What happens to the other
courses once it is taken?

</details>

<details><summary>Hint 3</summary>

Two different paths that lead to the same course do not block anything. Make sure your solution
does not treat that as a problem.

</details>
