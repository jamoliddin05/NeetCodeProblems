import math
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products, suffix_products = [1] * len(nums), [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix_products[i] = 1
                continue

            prefix_products[i] = nums[i - 1] * prefix_products[i - 1]

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                suffix_products[j] = 1
                continue

            suffix_products[j] = nums[j + 1] * suffix_products[j + 1]

        res = []
        for prefix, suffix in zip(prefix_products, suffix_products):
            res.append(prefix * suffix)

        return res


# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
