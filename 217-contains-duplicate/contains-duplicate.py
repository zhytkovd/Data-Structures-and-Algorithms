class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq_dict = {}

        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                return True

        return False