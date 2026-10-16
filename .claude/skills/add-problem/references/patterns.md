# tests.py problem-section recipes

Only the `==== problem ====` block of tests.py changes per problem. Returned `ListNode`/`TreeNode`
objects, tuples and sets are converted to plain lists automatically before `check()` sees them.
Helpers available: `make_list(values)`, `make_tree(level_order)`, `list_values(head)`,
`tree_values(root)`, `find_node(root, value)`,
`same(a, b)` (float-tolerant), `same_any_order(a, b, nested=False)`.

## Contents
- Plain function (default) · Any order · Linked list · Binary tree · In-place
- Node arguments (LCA) · Linked list cycle · Round trip (encode/decode, Codec)
- Several valid answers · Design classes · Graph clone · Random-pointer list

## Plain function
```python
def solve(nums, target):
    return Solution().twoSum(nums, target)
```
Parameter names of `solve` must match the names used in inputs.txt.

## Any order
```python
def check(got, expected, inputs):
    return same_any_order(got, expected)               # top k frequent, word search II
    # same_any_order(got, expected, nested=True)       # group anagrams, subsets, 3sum
```
Permutations: outer order free but inner order matters, so `nested=False`.

## Linked list
```python
from solution import Solution, ListNode

def solve(head):
    return list_values(Solution().reverseList(make_list(head)))   # list of lists: [make_list(v) for v in lists]
```
Wrap returned nodes in `list_values` / `tree_values`: they turn `None` into `[]`, which is how an
empty list or tree is written in inputs.txt.

## Binary tree
```python
def solve(root):
    return tree_values(Solution().invertTree(make_tree(root)))     # level order with null gaps
```

## In-place (method returns None)
```python
def solve(matrix):
    Solution().rotate(matrix)
    return matrix

def solve(head):                                        # reorder list
    head = make_list(head)
    Solution().reorderList(head)
    return list_values(head)
```

## Node arguments (lowest common ancestor)
```python
def solve(root, p, q):
    root = make_tree(root)
    node = Solution().lowestCommonAncestor(root, find_node(root, p), find_node(root, q))
    return node.val
```

## Linked list cycle (`index` = where the tail links back, -1 = no cycle)
```python
def solve(head, index):
    head = make_list(head)
    if index >= 0:
        nodes, node = [], head
        while node:
            nodes.append(node)
            node = node.next
        nodes[-1].next = nodes[index]
    return Solution().hasCycle(head)
```
The returned value is a bool, so `to_plain` never walks the cycle.

## Round trip
```python
def solve(strs):                                        # encode and decode strings
    s = Solution()
    return s.decode(s.encode(strs))

from solution import Codec                              # serialize / deserialize tree

def solve(root):
    codec = Codec()
    return tree_values(codec.deserialize(codec.serialize(make_tree(root))))
```

## Several valid answers (validate instead of comparing)
```python
def check(got, expected, inputs):                       # course schedule II
    if expected == []:
        return got == []
    n, prereqs = inputs["numCourses"], inputs["prerequisites"]
    if sorted(got) != list(range(n)):
        return False
    position = {course: i for i, course in enumerate(got)}
    return all(position[before] < position[after] for after, before in prereqs)
```

## Design classes
```python
from solution import MinStack

TITLE = "Min Stack"
DESIGN = True
```
inputs.txt then lists calls; the first line constructs the object:
```
# Example 1
MinStack()
push(1)
push(2)
getMin() -> 1
pop()
top() -> 1
```
`solve`/`check` are unused in design mode; keep the template's definitions.

## Graph clone (Node with neighbors, input is an adjacency list, nodes numbered from 1)
```python
from solution import Solution, Node

def solve(adjList):
    nodes = [Node(i + 1) for i in range(len(adjList))]
    for node, neighbours in zip(nodes, adjList):
        node.neighbors = [nodes[j - 1] for j in neighbours]
    clone = Solution().cloneGraph(nodes[0] if nodes else None)
    if clone is None:
        return []
    seen, order, queue = {clone.val: clone}, [], [clone]
    while queue:
        node = queue.pop()
        assert all(node is not original for original in nodes), "returned the original nodes, not a copy"
        for nb in node.neighbors:
            if nb.val not in seen:
                seen[nb.val] = nb
                queue.append(nb)
    return [[nb.val for nb in seen[v].neighbors] for v in sorted(seen)]
```

## Random-pointer list (input `[[val, random_index or null], ...]`)
```python
from solution import Solution, Node

def solve(head):
    nodes = [Node(val) for val, _ in head]
    for i, (_, rnd) in enumerate(head):
        nodes[i].next = nodes[i + 1] if i + 1 < len(nodes) else None
        nodes[i].random = nodes[rnd] if rnd is not None else None
    copy, out, index = Solution().copyRandomList(nodes[0] if nodes else None), [], {}
    node = copy
    while node:
        assert node not in nodes, "returned an original node, not a copy"
        index[id(node)] = len(out)
        out.append(node)
        node = node.next
    return [[n.val, index[id(n.random)] if n.random else None] for n in out]
```
