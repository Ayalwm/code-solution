class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            diff[end + 1] -= val
        
        res = []
        cur = 0
        
        for i in range(n):
            cur += diff[i]
            shift = cur % 26
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            res.append(chr(new_char + ord('a')))
        
        return "".join(res)