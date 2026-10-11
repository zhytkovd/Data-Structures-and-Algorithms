class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        sorted_dict = dict(sorted(freq_dict.items(), key = lambda x: -x[1]))
        
        return list(sorted_dict.keys())[:k]