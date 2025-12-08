# Last updated: 12/8/2025, 9:41:28 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
9        path = []
10        ans = []
11
12        def dfs(root):
13            if not root:
14                return
15            path.append(str(root.val))
16            if not root.left and not root.right:
17                ans.append("->".join(path))
18            else:
19                dfs(root.left)
20                dfs(root.right)
21            path.pop()
22
23        dfs(root)
24        return ans