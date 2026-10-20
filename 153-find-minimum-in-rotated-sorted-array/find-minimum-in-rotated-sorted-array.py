class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums) -1
        res = float(inf)

        while l<=r:
            if nums[l] < nums[r]: 
                res = min(nums[l],res)
                break

            m = (r+l)//2
            res = min(res,nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
