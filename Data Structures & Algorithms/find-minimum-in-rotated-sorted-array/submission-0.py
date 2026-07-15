class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_index = 0
        right_index = len(nums) - 1

        while left_index < right_index:
            
            if nums[left_index] < nums[right_index]:
                return nums[left_index]

            mid_index = left_index + (right_index - left_index) // 2

            if nums[mid_index] > nums[right_index]:
                left_index = mid_index + 1
            else:
                right_index = mid_index
        
        return nums[left_index]