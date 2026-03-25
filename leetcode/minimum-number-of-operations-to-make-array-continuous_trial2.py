class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))  
        
        ans = n
        left = 0
        
        for right in range(len(nums)):
            while nums[right] - nums[left] >= n:
                left += 1
            
            window_size = right - left + 1
            ans = min(ans, n - window_size)
        
        return ans