class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle_i = (r + l)//2 # floor division

            if nums[middle_i] > target:
                r = middle_i - 1
            elif nums[middle_i] < target:
                l = middle_i + 1
            else:
                return middle_i
        return -1
           