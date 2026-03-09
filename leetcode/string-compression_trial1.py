class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0  
        res = 0  
        
        while i < len(chars):
            group_char = chars[i]
            count = 0
            
            while i < len(chars) and chars[i] == group_char:
                i += 1
                count += 1
            
            chars[res] = group_char
            res += 1
            
            if count > 1:
                for digit in str(count):
                    chars[res] = digit
                    res += 1
                    
        return res