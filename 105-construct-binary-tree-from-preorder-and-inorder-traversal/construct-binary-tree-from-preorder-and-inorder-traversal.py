# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder: return None
        
        m = inorder.index(preorder[0]) # index - first element is always a root

        root = TreeNode(preorder[0])
        # l_inorder = inorder[0:m]
        # l_preorder = preorder[1:len(l_inorder)+1]
        root.left = self.buildTree(preorder[1:len(inorder[0:m])+1],inorder[0:m])
        # r_inorder = inorder[m+1:]
        # r_preorder = preorder[1+len(inorder[0:m]):]
        root.right = self.buildTree(preorder[1+len(inorder[0:m]):],inorder[m+1:])

        return root

