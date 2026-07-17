class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * (2 * length)

        for i in range(len(answer)):
            answer[i] = nums[i % length]
        
        return answer