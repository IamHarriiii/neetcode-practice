class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hasComplement = {}

        for index, value in enumerate(nums):
            complement = target - value

            if complement in hasComplement:
                return [hasComplement[complement], index]
            hasComplement[value] = index

        return []
            