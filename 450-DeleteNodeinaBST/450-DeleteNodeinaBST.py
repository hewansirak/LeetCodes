# Last updated: 5/14/2025, 11:10:42 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def getInOrderSucc(node):
            
            while node.left:
                node = node.left

            return node

        def deleteNode(node, key):
            if not node:
                return 

            if  key <  node.val:
                node.left = deleteNode(node.left,key) # None

            elif key > node.val:
                node.right = deleteNode(node.right,key)

            else:
                # case I
                if not node.left and not node.right:
                    return

                #case II
                if not node.left:
                    return node.right

                if not node.right:
                    return node.left

                
                #case III
                inOrderSucc = getInOrderSucc(node.right)
                node.val = inOrderSucc.val
                node.right = deleteNode(node.right,inOrderSucc.val)

            
            return node

        return deleteNode(root,key)
