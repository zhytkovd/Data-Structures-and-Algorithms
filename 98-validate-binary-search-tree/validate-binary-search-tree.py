# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low, up = float("-inf"),float("inf")
        
        def bst(root,low,up):
            if not root: return True

            if root.val > low and root.val < up:
                return bst(root.right,root.val,up) and bst(root.left,low,root.val)
            else:
                return False 

        return bst(root,low,up)