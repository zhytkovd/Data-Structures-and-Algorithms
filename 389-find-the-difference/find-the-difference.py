class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = {}

        if not s:
            return t

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else: 
                char_count[char] = 1
        
        for char in t:
            if (char not in char_count) or (char_count[char]==0) :
                return char
            else:
                char_count[char] -= 1
        
    

# we need to find the missing letter in the second string

# input: 2 strings
# output: 1 character

# solution:
# run a loop on the first and add all the chars to dict with count
# second loop: if char in the second loop, we skip, 
# if not, we return the character

# edge cases: 
# if s empty, return t


