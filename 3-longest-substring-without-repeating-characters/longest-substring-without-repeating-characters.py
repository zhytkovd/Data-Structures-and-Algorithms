class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l,r = 0, 0
        count = 0
        while r < len(s):

            if s[r] not in window:
                window.add(s[r])
             
                r += 1
                count = max(count,len(window)) 
            else:
                # if they are equal, we adjust left pointer and continue
                if s[l] == s[r]:
                    window.remove(s[l])
                    l += 1
                else:
                # if they are not equal we are using while loop to get to the duplicate value
                    while s[l] != s[r]:
                        window.remove(s[l])
                        l += 1
        return count 
            
