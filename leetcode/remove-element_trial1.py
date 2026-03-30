class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=len(nums)-1
        for i in range(l,-1,-1):            
            for j in range(i-1,-1,-1):
                if(val==nums[j] and val!=nums[i]):
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        count=nums.count(val)
        k=len(nums)-count

        return k