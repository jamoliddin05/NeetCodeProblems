from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            start_ptr, end_ptr = i + 1, len(nums) - 1

            while start_ptr < end_ptr:
                first_num, second_num = nums[start_ptr], nums[end_ptr]
                if first_num + second_num > target:
                    end_ptr -= 1
                    continue

                if first_num + second_num < target:
                    start_ptr += 1
                    continue

                if first_num + second_num == target:
                    result.append([nums[i], nums[start_ptr], nums[end_ptr]])
                    old_start_ptr = start_ptr
                    while start_ptr < end_ptr and nums[old_start_ptr] == nums[start_ptr]:
                        start_ptr += 1

        return result

if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
