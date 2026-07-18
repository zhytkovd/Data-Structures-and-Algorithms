class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        freq_count1 = {}
        freq_count2 = {}

        for char1 in s:
            if char1 in freq_count1:
                freq_count1[char1] +=1
            else:
                freq_count1[char1] = 1
        
        for char1 in t:
            if char1 in freq_count2:
                freq_count2[char1] +=1
            else:
                freq_count2[char1] = 1
        
        return freq_count1 == freq_count2
