---
name: add-problem
description: Mirror a NeetCode or LeetCode problem into this PyCharm project as its own folder — README.md with the statement, solution.py with the site's exact starter signature to type the answer into, inputs.txt with hand-written test cases (examples + edge cases), and tests.py that runs them and shows which case failed and why. Use whenever the user pastes a neetcode.io/problems/... or leetcode.com/problems/... link, or asks to add, set up, start or mirror a problem locally, even if they don't mention tests.
---

# Add a problem

The user solves problems locally in PyCharm and, once done, pastes `class Solution` back into the
site. So the folder has to mirror the site exactly, and the tests have to be good enough that
"all green locally" means "accepted" there.

## 1. Read the problem

Open the link once (WebFetch or the browser) and note: title, LeetCode number, difficulty,
statement, examples, constraints, hints / target complexity, and the **Python starter code**.
Copy the starter verbatim: NeetCode often renames LeetCode's methods (`hasDuplicate` vs
`containsDuplicate`), and the link the user gave is what they'll paste back into. If the page
can't be read, work from what you know about the problem and say the signature should be
double-checked.

## 2. Create the folder

`<project root>/<NNNN>_<snake_case_title>/`, e.g. `0217_contains_duplicate/` (LeetCode number,
zero-padded). Without a known number, use just the snake-case title. If the folder already
exists, never overwrite `solution.py` — it's the user's work; ask first.

### README.md
Title with number, difficulty, link(s), then the task restated clearly in your own words (don't
paste the site's text wholesale), the examples and constraints exactly as given, the target
complexity if the site states one, and a few short hints of your own inside
`<details><summary>Hint 1</summary>…</details>` so they stay hidden until wanted. No approach
spelled out, no solution.

### solution.py
The starter code, made runnable and nothing more:
- `from typing import List, Optional` (only the names it uses);
- `ListNode` / `TreeNode` / `Node` definitions **uncommented** (LeetCode comments them out because
  its judge provides them; locally they must exist);
- `pass` in each empty method body;
- at the very bottom, this block, so PyCharm's Run on `solution.py` runs the tests (the user
  copies only the class back to the site; the comment marks where to stop):

```python
# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
```

### inputs.txt
One case per block, blocks separated by a blank line, a `# name` line on top of each:

```
# Example 1
nums = [1, 2, 3, 3]
expected = true

# stress: 10^5 distinct numbers
nums = list(range(100000))
expected = false
```

Start the file with a short comment header explaining this format (the user adds their own
cases). Values are JSON (`true`, `null`, `"text"`) or Python expressions — handy for large
inputs. A case without `expected` just prints what the solution returns. Design problems use
one call per line instead (see references/patterns.md).

Write the statement's examples first (`Example 1`, …), then your own edge cases — 6–12 cases in
total. Think like the hidden test set: the smallest inputs the constraints allow (empty, one
element), all-equal values, negatives and zero, values at the constraint extremes, duplicates,
sorted / reverse-sorted input, and whatever breaks the tempting wrong approach for this problem
(off-by-one, greedy that fails, integer overflow assumptions). When the constraints are large
(n ≳ 10⁴) add one stress case at full size that a brute-force solution can't finish within the
time limit; build it so the answer is obvious by construction. Name every case by what it probes
(`# single element`, `# all negative`) — that name is what the user sees when it fails.

### tests.py
`assets/tests_template.md` (next to this file) holds the runner as one Python code block. Write
that block verbatim to `tests.py` and edit only the `==== problem ====` section: the import,
`TITLE`, `DESIGN`, `solve()` (how one case calls the solution — its parameter names match
inputs.txt) and, when equality isn't the right test, `check()`. The runner below that section
is generic; leave it alone. Extracting the block with a short script is safer than retyping it. References/patterns.md has ready
`solve`/`check` snippets for linked lists, trees, in-place methods, any-order answers, several
valid answers, round trips (encode/decode, Codec), design classes and node-based inputs — read
the one that matches before writing tests.py.

## 3. Verify the expected values

Hand-computed answers are where mistakes hide, and a wrong `expected` sends the user hunting a
bug that isn't there. So prove them:

1. Copy the folder to your scratchpad (or a temp dir), replace `solution.py` **in the copy** with
   a correct solution you write, and run `python tests.py` there — every case must pass. If one
   doesn't, work out whether the expected value or your solution is wrong before changing
   anything.
2. Run `python tests.py` in the real folder against the untouched stub: cases should fail
   cleanly (✗ with expected/got), proving the harness runs. Use the project's `.venv/bin/python`
   if it exists.

The correct solution never goes into the user's folder.

## 4. Report

Tell the user the folder path, how to run (Run `solution.py` in PyCharm, or `python solution.py`
/ `python tests.py`; add `3` for one case, `-x` to stop at the first failure), and a one-line list
of what the edge cases cover.
Don't hint at the approach.
