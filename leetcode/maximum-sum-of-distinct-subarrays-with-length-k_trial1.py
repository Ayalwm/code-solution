class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        cur_sum = 0
        seen = {}
        ans = 0
        
        for right in range(len(nums)):
            cur_sum += nums[right]
            seen[nums[right]] = seen.get(nums[right], 0) + 1
            
            if right - left + 1 > k:
                seen[nums[left]] -= 1
                cur_sum -= nums[left]
                if seen[nums[left]] == 0:
                    del seen[nums[left]]
                left += 1
            
            if right - left + 1 == k and len(seen) == k:
                ans = max(ans, cur_sum)
        
        return ans