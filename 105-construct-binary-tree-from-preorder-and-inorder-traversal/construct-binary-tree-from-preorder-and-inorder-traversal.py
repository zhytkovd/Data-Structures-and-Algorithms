# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder: return None

        root_val = preorder[0] # first element is always a root

        m = inorder.index(root_val)
        # pass values to the left
        l_inorder = inorder[0:m]
        l_preorder = preorder[1:len(l_inorder)+1]
        # pass values to the right
        r_inorder = inorder[m+1:]
        r_preorder = preorder[1+len(l_preorder):]

        return TreeNode(preorder[0],self.buildTree( l_preorder,l_inorder), self.buildTree(r_preorder,r_inorder))

