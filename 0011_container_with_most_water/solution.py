from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_ptr, right_ptr = 0, len(heights) - 1
        best_area = 0

        while left_ptr < right_ptr:
            area = min(heights[left_ptr], heights[right_ptr]) * (right_ptr - left_ptr)
            if area > best_area:
                best_area = area

            if heights[left_ptr] < heights[right_ptr]:
                left_ptr += 1
                continue

            if heights[left_ptr] > heights[right_ptr]:
                right_ptr -= 1
                continue

            if heights[left_ptr] == heights[right_ptr]:
                left_ptr += 1
                continue

        return best_area


# Local only: running this file runs tests.py. Don't paste this part into the site.
if __name__ == "__main__":
    import tests

    raise SystemExit(tests.main())
