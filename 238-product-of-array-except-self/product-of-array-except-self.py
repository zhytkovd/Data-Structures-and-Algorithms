class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        if len(nums) == 0: return []
        if len(nums) == 1: return nums
        
        #prefix computation: 
        prefix = [nums[0]]
        for i in range(0,len(nums)-1):
            prefix.append(prefix[i]*nums[i+1])

        #prefix computation: 
        suffix = [nums[len(nums)-1]]
        for i in range(len(nums)-1,0, -1 ):
            suffix.append(suffix[len(suffix)-1]*nums[i-1])
        suffix = suffix[::-1]

        res = [suffix[1]]
        for i in range(1,len(nums)-1):
            res.append(prefix[i-1]*suffix[i+1])

        res.append(prefix[len(nums)-2])

        return res
        
