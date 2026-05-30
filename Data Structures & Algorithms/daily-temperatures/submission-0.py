class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lengthOfTemps = len(temperatures)
        result = [0] * lengthOfTemps
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            
            stack.append(i)
        
        return result