class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2): # i + j + k = 0 => -k = i + j
            # skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # early exit: smallest value is positive, no way to reach 0
            if nums[i] > 0:
                break
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                # from 2 sum sorted
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicate values for l
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

            