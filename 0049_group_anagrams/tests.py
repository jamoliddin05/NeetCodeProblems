"""Runs every case from inputs.txt against solution.py and shows what failed.

    python tests.py                  all cases
    python tests.py 2 5              only cases #2 and #5
    python tests.py -x               stop at the first failure
"""
import argparse
import ast
import builtins
import contextlib
import io
import json
import math
import os
import random
import re
import signal
import sys
import time
import traceback
from collections import deque

# ==== problem ======================================================================
from solution import Solution

TITLE = "Group Anagrams"
DESIGN = False  # True: each inputs.txt line is a method call on one object (MinStack, LRUCache, ...)
TIME_LIMIT = 2.0  # seconds per case


def solve(strs):
    return Solution().groupAnagrams(strs)


def check(got, expected, inputs):
    return same_any_order(got, expected, nested=True)
# ===================================================================================

HERE = os.path.dirname(os.path.abspath(__file__))
SOLUTION = sys.modules["solution"]
SOLUTION_PATH = os.path.abspath(SOLUTION.__file__)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TimedOut(BaseException):
    """BaseException so an `except Exception` in the solution can't swallow it."""


# ---- helpers for solve() / check() ------------------------------------------------

def make_list(values):
    node_class = getattr(SOLUTION, "ListNode", ListNode)
    dummy = tail = node_class(0)
    for value in values:
        tail.next = node_class(value)
        tail = tail.next
    return dummy.next


def make_tree(values):
    node_class = getattr(SOLUTION, "TreeNode", TreeNode)
    if not values or values[0] is None:
        return None
    root = node_class(values[0])
    queue, i = deque([root]), 1
    while queue and i < len(values):
        node = queue.popleft()
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                child = node_class(values[i])
                setattr(node, side, child)
                queue.append(child)
            i += 1
    return root


def find_node(root, value):
    queue = deque([root] if root else [])
    while queue:
        node = queue.popleft()
        if node.val == value:
            return node
        queue.extend(child for child in (node.left, node.right) if child)
    raise ValueError(f"no node with value {value!r} in the tree")


def list_values(head):
    """Linked list -> [values]; None is the empty list."""
    values, seen = [], set()
    while head is not None:
        if id(head) in seen:
            raise ValueError(f"the returned linked list has a cycle (starts {values[:10]})")
        seen.add(id(head))
        values.append(head.val)
        head = head.next
    return values


def tree_values(root):
    """Tree -> LeetCode level order with null gaps; None is the empty tree."""
    values, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        values.append(None if node is None else node.val)
        if node is not None:
            queue.extend((node.left, node.right))
        if len(values) > 10 ** 6:
            raise ValueError("the returned tree has a cycle")
    while values and values[-1] is None:
        values.pop()
    return values


def to_plain(x):
    """Returned nodes, tuples and sets become the list values used in inputs.txt."""
    if isinstance(x, (list, tuple)):
        return [to_plain(v) for v in x]
    if isinstance(x, (set, frozenset)):
        return sort_any([to_plain(v) for v in x])
    if hasattr(x, "val") and hasattr(x, "left") and hasattr(x, "right"):
        return tree_values(x)
    if hasattr(x, "val") and hasattr(x, "next"):
        return list_values(x)
    return x


def sort_any(items):
    try:
        return sorted(items)
    except TypeError:
        return sorted(items, key=repr)


def same(a, b):
    """Equality with float tolerance, recursing into lists."""
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
    if isinstance(a, float) or isinstance(b, float):
        try:
            return math.isclose(a, b, rel_tol=1e-5, abs_tol=1e-5)
        except TypeError:
            return False
    return a == b


def same_any_order(a, b, nested=False):
    """Order of the outer list doesn't matter; with nested=True neither does the order inside each item."""
    if not (isinstance(a, list) and isinstance(b, list)):
        return same(a, b)
    if nested:
        a = [sort_any(x) if isinstance(x, list) else x for x in a]
        b = [sort_any(x) if isinstance(x, list) else x for x in b]
    return same(sort_any(a), sort_any(b))


# ---- reading inputs.txt ---------------------------------------------------------------

SAFE_BUILTINS = {name: getattr(builtins, name) for name in (
    "range", "list", "tuple", "dict", "set", "str", "int", "float", "bool", "len", "min", "max",
    "sum", "abs", "sorted", "reversed", "zip", "map", "enumerate", "chr", "ord",
)}


def parse_value(src):
    """JSON (true/false/null) first, then Python literals, then an expression like list(range(10**5))."""
    try:
        return json.loads(src)
    except ValueError:
        pass
    try:
        return ast.literal_eval(src)
    except (ValueError, SyntaxError):
        pass
    # Seeded from the text itself, so random test data is identical on every run.
    scope = {"__builtins__": SAFE_BUILTINS, "random": random.Random(src), "true": True, "false": False, "null": None}
    try:
        return eval(src, scope)
    except Exception as e:
        raise ValueError(f"can't read value {short(src, 80)}: {e}") from None


def split_call(line):
    """'put(1, 10) -> null' -> ('put', '1, 10', 'null')"""
    name, paren, rest = line.partition("(")
    depth, quote = 1, None
    for i, ch in enumerate(rest):
        if quote:
            quote = None if ch == quote and rest[i - 1] != "\\" else quote
        elif ch in "\"'":
            quote = ch
        elif ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
            if depth == 0:
                tail = rest[i + 1:].strip()
                if tail and not tail.startswith("->"):
                    break
                return name.strip(), rest[:i], tail[2:].strip() if tail else None
    raise ValueError(f"expected `method(args) -> expected`, got {line!r}")


def parse_cases(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    cases, number = [], 0
    for block in re.split(r"\n[ \t]*\n", text):
        lines = [(i, line.strip()) for i, line in enumerate(block.splitlines()) if line.strip()]
        body = [line for _, line in lines if not line.startswith("#")]
        if not body:
            continue
        number += 1
        names = [line[1:].strip() for _, line in lines if line.startswith("#")]
        case = {"number": number, "name": names[0] if names else "", "inputs": {}, "expected": None,
                "calls": [], "error": None}
        try:
            for line in body:
                if DESIGN:
                    case["calls"].append(split_call(line))
                    continue
                key, sep, src = line.partition("=")
                if not sep or not key.strip().isidentifier():
                    raise ValueError(f"expected `name = value`, got {line!r}")
                if key.strip() == "expected":
                    case["expected"] = src.strip()
                else:
                    case["inputs"][key.strip()] = src.strip()
        except ValueError as e:
            case["error"] = str(e)
        cases.append(case)
    return cases


# ---- running ---------------------------------------------------------------------

@contextlib.contextmanager
def time_limit(seconds):
    # Under a debugger the clock keeps running while paused, so every case would time out.
    if not hasattr(signal, "SIGALRM") or sys.gettrace() or "pydevd" in sys.modules:
        yield
        return

    def expire(signum, frame):
        raise TimedOut()

    previous = signal.signal(signal.SIGALRM, expire)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def describe_error(exc):
    frames = traceback.extract_tb(exc.__traceback__)
    own = [f for f in frames if os.path.abspath(f.filename) == SOLUTION_PATH]
    frame = (own or frames)[-1] if frames else None
    text = f"{type(exc).__name__}: {exc}"
    if frame:
        text += f"\n  at {os.path.basename(frame.filename)}:{frame.lineno}  ->  {(frame.line or '').strip()}"
    return text


def run(case):
    """Returns (status, got, expected_src, message, call_index, seconds, stdout)."""
    if case["error"]:
        return "INPUT", None, None, case["error"], None, 0.0, ""
    out = io.StringIO()
    try:
        if DESIGN:
            steps = [(name, parse_value(f"[{args}]"), None if exp is None else parse_value(exp))
                     for name, args, exp in case["calls"]]
        else:
            inputs = {name: parse_value(src) for name, src in case["inputs"].items()}
            expected = None if case["expected"] is None else parse_value(case["expected"])
    except ValueError as e:
        return "INPUT", None, None, str(e), None, 0.0, ""

    start, index = time.perf_counter(), 0
    try:
        with contextlib.redirect_stdout(out), time_limit(TIME_LIMIT):
            if DESIGN:
                obj, results = None, []
                for index, (name, args, exp) in enumerate(steps):
                    if index == 0:
                        obj = getattr(SOLUTION, name)(*args)
                        continue
                    got = to_plain(getattr(obj, name)(*args))
                    results.append(got)
                    if exp is not None and not same(got, exp):
                        return ("FAIL", got, case["calls"][index][2], "", index,
                                time.perf_counter() - start, out.getvalue())
                got = results
            else:
                got = to_plain(solve(**inputs))
    except TimedOut:
        return "TIMEOUT", None, None, "", index, TIME_LIMIT, out.getvalue()
    except Exception as e:
        return "ERROR", None, None, describe_error(e), index, time.perf_counter() - start, out.getvalue()
    elapsed = time.perf_counter() - start

    if DESIGN:
        checked = any(exp is not None for _, _, exp in steps)
        return ("PASS" if checked else "UNCHECKED"), got, None, "", None, elapsed, out.getvalue()
    if case["expected"] is None:
        return "UNCHECKED", got, None, "", None, elapsed, out.getvalue()
    try:
        ok = check(got, expected, inputs)
    except Exception as e:
        return "FAIL", got, case["expected"], f"check() failed: {e}", None, elapsed, out.getvalue()
    return ("PASS" if ok else "FAIL"), got, case["expected"], "", None, elapsed, out.getvalue()


# ---- reporting --------------------------------------------------------------------

COLOR = (sys.stdout.isatty() or "PYCHARM_HOSTED" in os.environ) and "NO_COLOR" not in os.environ
MARKS = {"PASS": ("✓", "32"), "FAIL": ("✗", "31"), "ERROR": ("!", "31"), "TIMEOUT": ("⏱", "33"),
         "INPUT": ("?", "35"), "UNCHECKED": ("·", "36")}


def paint(text, code):
    return f"\033[{code}m{text}\033[0m" if COLOR else text


def short(text, limit=300):
    text = str(text)
    return text if len(text) <= limit else f"{text[:limit]}… ({len(text)} chars)"


def show(value):
    try:
        return short(json.dumps(value, ensure_ascii=False))
    except (TypeError, ValueError):
        return short(repr(value))


def label(case):
    return f"#{case['number']}" + (f" {case['name']}" if case["name"] else "")


def report(case, status, got, expected_src, message, call_index, elapsed, stdout, label_width=50):
    mark, color = MARKS[status]
    timing = f"TIMEOUT > {TIME_LIMIT:g} s" if status == "TIMEOUT" else f"{elapsed * 1000:.2f} ms"
    print(f"  {paint(mark, color)} {label(case):<{label_width}}  {paint(timing, '2')}")
    if status == "PASS":
        return

    pad = "      "
    width = max([len(name) for name in case["inputs"]] + [len("expected")])
    if DESIGN:
        last = call_index if call_index is not None else len(case["calls"]) - 1
        first = max(0, last - 8)
        if first:
            print(paint(f"{pad}… {first} earlier calls", "2"))
        for i, (name, args, _) in enumerate(case["calls"][first:last + 1], first):
            line = f"{name}({short(args, 120)})"
            if status == "UNCHECKED" and i and got[i - 1] is not None:
                line += f"  -> {show(got[i - 1])}"
            print(f"{pad}{'→ ' if i == call_index else '  '}{line}")
    else:
        for name, src in case["inputs"].items():
            print(f"{pad}{name:<{width}} = {short(src)}")

    if status in ("FAIL", "UNCHECKED") and not (DESIGN and status == "UNCHECKED"):
        if expected_src is not None:
            print(f"{pad}{'expected':<{width}} = {paint(short(expected_src), '32')}")
        name = "got" if status == "FAIL" else "returns"
        hint = "   (nothing returned — missing `return`?)" if got is None else ""
        print(f"{pad}{name:<{width}} = {paint(show(got), color)}{paint(hint, '2')}")
    for line in message.splitlines():
        print(f"{pad}{paint(line, '31')}")
    if status == "TIMEOUT":
        print(paint(f"{pad}too slow or an infinite loop — compare with the target complexity in README.md", "33"))
    if stdout.strip():
        lines = stdout.rstrip().splitlines()
        print(paint(f"{pad}your prints:", "2"))
        for line in lines[:20]:
            print(paint(f"{pad}  {short(line, 200)}", "2"))
        if len(lines) > 20:
            print(paint(f"{pad}  … {len(lines) - 20} more lines", "2"))


def main():
    parser = argparse.ArgumentParser(description=f"Run inputs.txt against a {TITLE} solution.")
    parser.add_argument("cases", nargs="*", type=int, help="case numbers to run (default: all)")
    parser.add_argument("-x", "--exitfirst", action="store_true", help="stop at the first failing case")
    opts = parser.parse_args()
    sys.setrecursionlimit(max(sys.getrecursionlimit(), 10_000))


    cases = parse_cases(os.path.join(HERE, "inputs.txt"))
    if opts.cases:
        cases = [c for c in cases if c["number"] in opts.cases]
    print(paint(f"{TITLE} — {len(cases)} case{'s' if len(cases) != 1 else ''}", "1"))
    label_width = min(max([len(label(c)) for c in cases] + [10]), 64)
    counts = dict.fromkeys(MARKS, 0)
    for case in cases:
        result = run(case)
        counts[result[0]] += 1
        report(case, *result, label_width=label_width)
        if opts.exitfirst and result[0] not in ("PASS", "UNCHECKED"):
            break

    ran = sum(counts.values())
    failed = ran - counts["PASS"] - counts["UNCHECKED"]
    summary = [f"{counts['PASS']}/{ran} passed"]
    summary += [f"{counts[s]} {s.lower()}" for s in ("FAIL", "ERROR", "TIMEOUT", "INPUT", "UNCHECKED") if counts[s]]
    print("\n" + paint(", ".join(summary), "31;1" if failed else "32;1"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
