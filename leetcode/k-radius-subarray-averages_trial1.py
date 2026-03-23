class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        avgs = [-1] * n
        
        if n < window_size:
            return avgs
        
        current_window_sum = sum(nums[:window_size])
        
        avgs[k] = current_window_sum // window_size
        
        for i in range(k + 1, n - k):
            current_window_sum = current_window_sum - nums[i - k - 1] + nums[i + k]
            avgs[i] = current_window_sum // window_size
            
        return avgs