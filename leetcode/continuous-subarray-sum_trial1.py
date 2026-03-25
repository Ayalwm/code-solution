class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}  
        total = 0
        
        for i, num in enumerate(nums):
            total += num
            r = total % k
            
            if r in remainder_map:
                if i - remainder_map[r] > 1:
                    return True
            else:
                remainder_map[r] = i
        
        return False