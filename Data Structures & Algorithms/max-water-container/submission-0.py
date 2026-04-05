class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_index = 0
        right_index = len(heights) - 1
        max_water = 0

        while left_index < right_index:
            width = right_index - left_index
            height = min(heights[left_index], heights[right_index])
            max_water = max(max_water, (width * height))

            if heights[left_index] < heights[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return max_water