from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            freq_key = self.get_freq_key(s)
            groups.setdefault(freq_key, []).append(s)

        return list(groups.values())

    def get_freq_key(self, s: str) -> tuple[int, ...]:
        freq_key_pattern = [0] * 26
        for char in s:
            freq_key_pattern[ord(char) - ord("a")] += 1

        return tuple(freq_key_pattern)



# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
