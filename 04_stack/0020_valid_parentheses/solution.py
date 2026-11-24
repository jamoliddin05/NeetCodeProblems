class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_pairs = {
            '}': '{',
            ')': '(',
            ']': '[',
        }

        stack = []

        for char in s:
            if char in parentheses_pairs and len(stack) != 0 and stack[-1] == parentheses_pairs[char]:
                stack.pop()
                continue

            stack.append(char)

        return len(stack) == 0

# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
