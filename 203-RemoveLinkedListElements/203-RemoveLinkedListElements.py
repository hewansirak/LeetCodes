# Last updated: 4/15/2025, 10:40:42 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        currNode = dummy_node

        while currNode.next: # dummyNode #[7,7,7,7]
            if currNode.next.val == val: # 2
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next

        return dummy_node.next