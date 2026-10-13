class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r = 0, (len(numbers) -1)

        while l <= r:
            if (numbers[r] + numbers[l]) > target: 
                r -= 1
            if (numbers[r] + numbers[l]) < target: 
                l += 1
            if (numbers[r] + numbers[l]) == target: return [l+1,r+1]
        