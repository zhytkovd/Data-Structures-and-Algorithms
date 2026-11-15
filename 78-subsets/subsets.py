class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = [] 
        subset = []

        def dfs(i):
            if i >= len(nums): #base case
                res.append(subset.copy())
                return
            
            # adding value
            subset.append(nums[i])
            dfs(i+1)

            # removing value
            subset.pop()
            dfs(i+1)
        
        dfs(0)

        return res