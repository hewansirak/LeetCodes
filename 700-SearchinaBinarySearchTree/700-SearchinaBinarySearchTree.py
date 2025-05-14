# Last updated: 5/14/2025, 9:00:23 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def searchBST(node):    
            if not node:
                return
            
            if val < node.val:
                return searchBST(node.left)

            if val > node.val:
                return searchBST(node.right)

            if val == node.val:
                return node
        
        return searchBST(root)
