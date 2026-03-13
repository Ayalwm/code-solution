class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window = n - k
        total = sum(cardPoints)
        
        if window == 0:
            return total
        
        cur = sum(cardPoints[:window])
        min_sum = cur
        
        for i in range(window, n):
            cur += cardPoints[i]
            cur -= cardPoints[i - window]
            min_sum = min(min_sum, cur)
        
        return total - min_sum