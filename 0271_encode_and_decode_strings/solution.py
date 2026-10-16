from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for s in strs:
            parts.append(f"{len(s)}#{s}")
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        char_length = 0
        while i < len(s):
            if s[i] == "#":
                length = int(s[i - char_length:i])
                res.append(s[i+1:i+length+1])
                i += length + 1
                char_length = 0
                continue

            i += 1
            char_length += 1

        return res


# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
