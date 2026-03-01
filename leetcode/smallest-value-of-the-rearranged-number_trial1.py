class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        s = list(str(abs(num)))
        
        if num > 0:
            s.sort()
            if s[0] == '0':
                for i in range(len(s)):
                    if s[i] != '0':
                        s[0], s[i] = s[i], s[0]
                        break
            return int("".join(s))
        else:
            s.sort(reverse=True)
            return -int("".join(s))