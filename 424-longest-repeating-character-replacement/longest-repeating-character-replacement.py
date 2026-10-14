class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        res = 0
        l,r = 0, 0
        n = len(s)
        while r < n:
            if s[r] not in d: 
                d[s[r]] = 1
            else:
                d[s[r]] += 1
            win_len = r-l+1

            if (win_len - max(d.values())) <= k:
                res = max(res,win_len)
            else:
                if d[s[l]] == 1: del d[s[l]]
                else: d[s[l]] = d[s[l]] - 1
                l += 1
                
            r+=1
        return res