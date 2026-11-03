from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_ptr, end_ptr = 0, len(numbers) - 1
        first_num, second_num = numbers[start_ptr], numbers[end_ptr]

        while first_num + second_num != target:
            if first_num + second_num > target:
                end_ptr -= 1
                second_num = numbers[end_ptr]
                continue

            if first_num + second_num < target:
                start_ptr += 1
                first_num = numbers[start_ptr]
                continue

        return [start_ptr+1, end_ptr+1]




# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
