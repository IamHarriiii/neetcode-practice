class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sPointer = 0
        tPointer = 0

        while sPointer < len(s) and tPointer < len(t):
            if t[tPointer] == s[sPointer]:
                tPointer += 1
            sPointer += 1
        
        return len(t) - tPointer