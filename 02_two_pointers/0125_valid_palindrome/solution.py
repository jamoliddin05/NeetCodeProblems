class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c.lower() for c in s if c.isalnum())

        for i in range(len(cleaned)):
            if cleaned[i] != cleaned[len(cleaned) - 1 - i]:
                return False

        return True


# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
