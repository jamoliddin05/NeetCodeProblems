from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup_set = set(nums)
        longest_seq = 0
        curr_seq = 0

        for num in nums:
            if num - 1 not in lookup_set:
                i = 0
                while True:
                    curr_seq_num = num + i
                    if curr_seq_num in lookup_set:
                        i += 1
                        continue

                    break

                curr_seq += i
                continue

            longest_seq = max(longest_seq, curr_seq)

        return longest_seq

# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
