class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        l,r = 0, len(height)-1

        while l < r:
            volume = (min(height[l],height[r]))*(r-l)
            res = max(res,volume)

            if height[l] < height[r]: l+=1
            elif height[l] > height[r]: r-=1
            else:
                l+=1
                r-=1
        return res
                
        
        

            


        