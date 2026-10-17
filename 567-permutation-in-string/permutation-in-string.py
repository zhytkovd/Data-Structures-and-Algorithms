class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        d1 = {}
        d2 = {}
        for i in range(97,123):# a - 97, z - 122
            d1[chr(i)] = 0
            d2[chr(i)] = 0
        
        for i in s1:
            d1[i] += 1
        
        l = 0
        r = len(s1) -1

        for i in range(0,r+1):
            d2[s2[i]] += 1


        if d1 == d2: return True

        while r < len(s2)-1:
            l+=1
            r+=1
        
            d2[s2[l-1]] -= 1
            d2[s2[r]] += 1
            if d1 == d2: return True

        return False