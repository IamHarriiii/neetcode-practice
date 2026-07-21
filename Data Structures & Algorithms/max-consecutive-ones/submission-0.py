class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutiveOnes, consecutive = 0, 0
        for num in nums:
            if num == 1:
                consecutive += 1
            else:
                consecutive = 0
            consecutiveOnes = max(consecutiveOnes, consecutive)
        
        return consecutiveOnes