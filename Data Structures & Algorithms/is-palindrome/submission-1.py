class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            if not s[left_index].isalnum():
                left_index += 1
                continue
            
            if not s[right_index].isalnum():
                right_index -= 1
                continue

            if s[left_index] != s[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True