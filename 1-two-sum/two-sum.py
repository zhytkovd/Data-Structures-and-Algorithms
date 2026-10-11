class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        
        for i in range(len(nums)):
            dif = target - nums[i]
            
            if nums[i] in d:
                return [i,d[nums[i]]]
            else:
                d[dif] = i 
        