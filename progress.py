"""Runs every problem's tests and rewrites README.md with a ✓ next to each solved problem.

    python progress.py
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
NAMES = {
    "arrays_hashing": "Arrays & Hashing", "two_pointers": "Two Pointers", "sliding_window": "Sliding Window",
    "stack": "Stack", "binary_search": "Binary Search", "linked_list": "Linked List", "trees": "Trees",
    "tries": "Tries", "heap": "Heap / Priority Queue", "backtracking": "Backtracking", "graphs": "Graphs",
    "advanced_graphs": "Advanced Graphs", "dp_1d": "1-D Dynamic Programming", "dp_2d": "2-D Dynamic Programming",
    "greedy": "Greedy", "intervals": "Intervals", "math_geometry": "Math & Geometry",
    "bit_manipulation": "Bit Manipulation",
}
RANK = {"Easy": 0, "Medium": 1, "Hard": 2}


def is_solved(folder):
    result = subprocess.run([sys.executable, "tests.py"], cwd=folder, capture_output=True, text=True,
                            env={**os.environ, "NO_COLOR": "1", "PYTHONDONTWRITEBYTECODE": "1"})
    lines = result.stdout.strip().splitlines()
    return result.returncode == 0 and bool(lines) and re.fullmatch(r"(\d+)/\1 passed", lines[-1].strip()) is not None


def problem_row(topic, name):
    text = open(os.path.join(ROOT, topic, name, "README.md"), encoding="utf-8").read()
    title = text.splitlines()[0].lstrip("# ").strip()
    difficulty = re.search(r"\b(Easy|Medium|Hard)\b", text).group(1)
    link = re.search(r"https://leetcode\.com/problems/[a-z0-9-]+/?", text).group(0)
    source = "NeetCode" if "neetcode.io" in text else "LeetCode list"
    return difficulty, int(name.split("_")[0]), title, link, source


def main():
    topics = sorted(t for t in os.listdir(ROOT) if re.fullmatch(r"\d\d_\w+", t) and os.path.isdir(os.path.join(ROOT, t)))
    sections, total, solved_total = [], 0, 0
    for topic in topics:
        rows = []
        for name in os.listdir(os.path.join(ROOT, topic)):
            folder = os.path.join(ROOT, topic, name)
            if not os.path.exists(os.path.join(folder, "tests.py")):
                continue
            difficulty, number, title, link, source = problem_row(topic, name)
            solved = is_solved(folder)
            print(f"{'✓' if solved else ' '} {topic}/{name}")
            rows.append((RANK[difficulty], number, solved,
                         f"| {'✓' if solved else ''} | [{title}]({topic}/{name}/) | {difficulty} | [link]({link}) | {source} |"))
        rows.sort()
        done = sum(r[2] for r in rows)
        total += len(rows)
        solved_total += done
        sections += [f"## {topic[:2]} · {NAMES.get(topic[3:], topic[3:])} · {done}/{len(rows)} solved", "",
                     "| Solved | Problem | Difficulty | LeetCode | Set |", "|:-:|---|---|---|---|"]
        sections += [r[3] for r in rows] + [""]

    header = [
        "# LeetCode practice", "",
        "Problems grouped by topic. Each folder has `README.md` (the task), `solution.py` (write your answer here),",
        "`inputs.txt` (test cases) and `tests.py`. Run `solution.py` in PyCharm, or `python tests.py` inside the folder;",
        "`python tests.py 3` runs one case, `-x` stops at the first failure.", "",
        "A ✓ means every test case passes. Run `python progress.py` after solving a problem to update the ticks.", "",
        f"**Solved: {solved_total} of {total}.**", "",
    ]
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(header + sections).rstrip() + "\n")
    print(f"\nSolved {solved_total} of {total}. README.md updated.")


if __name__ == "__main__":
    main()
