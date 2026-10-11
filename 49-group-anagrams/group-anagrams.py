class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 0: return [[""]]
        d = {}

        for i in range(len(strs)):
            l = [0 for i in range(26)]

            for s in range(len(strs[i])):
                l[97 - int(ord(strs[i][s]))] += 1
            
            t = tuple(l)
            if t in d: 
                d[t].append(strs[i])
            else:
                d[t] = [strs[i]]

        return list(d.values())
