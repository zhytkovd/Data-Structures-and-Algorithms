# input: 2d list
# output: True, False

# edge cases:
# target < [0][0] or target is > [-1][-1]

# Plan: 
# double binary search
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        top, bottom = 0, len(matrix) -1

        while top <= bottom: # runs binary sort on first and last element of each row
            middle = (top+bottom)//2
            if (target >= matrix[middle][0]) and (target <= matrix[middle][-1]):
                break
            elif target < matrix[middle][0]:
                bottom = middle - 1
            elif target > matrix[middle][-1]:
                top = middle + 1

        l, r = 0, len(matrix[middle]) -1

        while l <= r:
            mid = (l+r) //2

            if target > matrix[middle][mid]:
                l = mid + 1
            elif target < matrix[middle][mid]:
                r = mid - 1
            else:
                return True
                
        return False

