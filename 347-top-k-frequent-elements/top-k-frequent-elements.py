class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = {}

        for num in nums:
            if num in freq_dict:
                freq_dict[num] += 1
            else:
                freq_dict[num] = 1

        freq = [[] for i in range(len(nums)+1)]

        for num in freq_dict.keys():
            freq[freq_dict[num]].append(num)
        
        res = []
        for li in range(len(freq)-1,0,-1): 
            for j in freq[li]:
                res.append(j)
                if len(res) == k: return res

        return res