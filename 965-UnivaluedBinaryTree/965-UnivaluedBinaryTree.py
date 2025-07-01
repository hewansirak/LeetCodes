# Last updated: 7/1/2025, 9:32:55 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
             return True 

        reference_value = root.val
        queue = collections.deque([root])

        while queue:
            current_node = queue.popleft()

            if current_node.val != reference_value:
                return False

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return True
