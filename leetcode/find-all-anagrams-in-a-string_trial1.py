from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:np])
        
        result = []
        
        if s_count == p_count:
            result.append(0)
            
        for i in range(np, ns):
            s_count[s[i]] += 1
            
            leaving_char = s[i - np]
            if s_count[leaving_char] == 1:
                del s_count[leaving_char]
            else:
                s_count[leaving_char] -= 1
            
            if s_count == p_count:
                result.append(i - np + 1)
                
        return result