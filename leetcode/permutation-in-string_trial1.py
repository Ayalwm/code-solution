class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        from collections import Counter
        
        need = Counter(s1)
        window = Counter()
        
        k = len(s1)
        
        for i in range(len(s2)):
            window[s2[i]] += 1
            
            if i >= k:
                if window[s2[i - k]] == 1:
                    del window[s2[i - k]]
                else:
                    window[s2[i - k]] -= 1
            
            if window == need:
                return True
        
        return False