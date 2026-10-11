class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = {}

        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1

        l = dict(sorted(freq_dict.items(), key = lambda x: -x[1]))
        
        return list(l.keys())[:k]