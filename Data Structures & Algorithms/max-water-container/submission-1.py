class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_index, right_index, width, height, max_water = 0, len(heights) - 1, 0, 0, 0

        while left_index < right_index:
            width = right_index - left_index
            height = min(heights[right_index], heights[left_index])
            max_water = max(max_water, (width * height))

            if heights[left_index] < heights[right_index]:
                left_index += 1
            else:
                right_index -= 1
        
        return max_water