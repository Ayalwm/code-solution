class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                whites += 1
        
        ans = whites
        
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                whites += 1
            if blocks[i - k] == 'W':
                whites -= 1
            
            ans = min(ans, whites)
        
        return ans