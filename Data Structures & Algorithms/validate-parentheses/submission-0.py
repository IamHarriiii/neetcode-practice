class Solution:
    def isValid(self, s: str) -> bool:
        
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []

        for ch in s:
            if ch in bracket_map.values():
                stack.append(ch)
            else:
                if not stack:
                    return False
                top_element = stack.pop()
                if top_element != bracket_map[ch]:
                    return False
        
        return (len(stack) == 0)