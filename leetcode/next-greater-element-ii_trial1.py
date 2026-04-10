class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        
        for i in range(2 * n):
            num = nums[i % n]
            
            while stack and nums[stack[-1]] < num:
                prev_index = stack.pop()
                res[prev_index] = num
            
            if i < n:
                stack.append(i)
                
        return res