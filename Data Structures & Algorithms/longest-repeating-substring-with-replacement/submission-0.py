class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_freq = defaultdict(int)
        left = 0
        max_freq = 0
        longest = 0
        
        for right in range(len(s)):
            character_freq[s[right]] += 1

            max_freq = max(max_freq, character_freq[s[right]])

            while ((right - left + 1) - max_freq > k):
                character_freq[s[left]] -= 1
                left += 1
            
            longest = max(longest, (right - left + 1))
        
        return longest
