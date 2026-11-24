from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup_set = set(nums)
        longest_seq = 0

        for num in lookup_set:
            if num - 1 not in lookup_set:
                curr_seq = 0
                while True:
                    curr_seq_num = num + curr_seq
                    if curr_seq_num in lookup_set:
                        curr_seq += 1
                        continue

                    break

                longest_seq = max(longest_seq, curr_seq)

        return longest_seq

# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
