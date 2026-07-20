class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestSoFar = -1

        for i in range(len(arr) - 1, -1, -1):
            currentValue = arr[i]
            arr[i] = greatestSoFar
            greatestSoFar = max(greatestSoFar, currentValue)
        
        return arr