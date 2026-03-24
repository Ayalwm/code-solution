class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        left = 0
        pairs = 0
        ans = 1
        
        for right in range(1, len(s)):
            if s[right] == s[right - 1]:
                pairs += 1
            
            while pairs > 1:
                if s[left] == s[left + 1]:
                    pairs -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans