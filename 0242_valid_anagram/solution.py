class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d1 = {}
        d2 = {}
        for a, b in zip(s, t):
            d1[a] = d1.get(a, 0) + 1
            d2[b] = d2.get(b, 0) + 1

        return d1 == d2

# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
