from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
