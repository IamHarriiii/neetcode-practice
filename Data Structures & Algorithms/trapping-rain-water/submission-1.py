class Solution:
    def trap(self, height: List[int]) -> int:
        left_index, right_index, left_max, right_max, max_water = 0, len(height) - 1, 0, 0, 0

        while left_index < right_index:
            if height[left_index] < height[right_index]:
                if height[left_index] >= left_max:
                    left_max = height[left_index]
                else:
                    max_water += left_max - height[left_index]
                left_index += 1
            else:
                if height[right_index] >= right_max:
                    right_max = height[right_index]
                else:
                    max_water += right_max - height[right_index]
                right_index -= 1
        
        return max_water