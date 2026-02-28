class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max=0
        j = len(piles)-2
        for i in range(int(len(piles)/3)):
            max += piles[j]
            j=j-2
        return max