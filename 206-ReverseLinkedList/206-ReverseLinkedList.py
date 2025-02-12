# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        rev = []
        while head:
            rev.append(head.val)
            head = head.next
        rev = rev[::-1]
        my_head = ListNode()
        pointer = my_head
        for i in rev:
            temp = ListNode(i)
            pointer.next = temp
            pointer = temp
        
        return my_head.next