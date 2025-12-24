# Last updated: 12/24/2025, 10:42:00 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9
10        def symmetry(l,r):
11            if not l and not r:
12                return True
13            if not l or not r or l.val!=r.val:
14                return False
15            
16            return symmetry(l.left,r.right) and symmetry(l.right,r.left)
17        return symmetry(root,root)