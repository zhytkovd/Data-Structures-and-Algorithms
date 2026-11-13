# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self,root1,root2): # -> bool
        if not root1 and not root2: return True # reached the end of the subtree
        if not root1 or not root2: return False # subtree has values, but root1 doesn't

        print("sameTree:",root1.val,root2.val)

        if root1.val != root2.val: return False
        
        return self.sameTree(root1.right,root2.right) and self.sameTree(root1.left,root2.left)


    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not root: return False
        print("Num of runs", self.isSubtree(root.left,subRoot) )

        if root.val == subRoot.val:
            print("isSubTree:",root.val,subRoot.val)
            if self.sameTree(root,subRoot):
                return True
                
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)

        
