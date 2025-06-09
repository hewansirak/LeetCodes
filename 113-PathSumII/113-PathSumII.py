# Last updated: 6/9/2025, 10:58:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        root.val = [root.val]
        res = []
        while stack:
            curr = stack.pop()
            if not curr.left and not curr.right:
                if sum(curr.val) == targetSum:
                    res.append(curr.val)

            if curr.left:
                stack.append(curr.left)
                curr.left.val = curr.val + [curr.left.val]
            if curr.right:
                stack.append(curr.right)
                curr.right.val = curr.val + [curr.right.val]

        return res