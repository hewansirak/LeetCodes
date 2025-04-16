# Last updated: 4/16/2025, 9:15:43 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        fast, slow = dummy, dummy
        index = 0

        while fast: # dummy index = 0, fast = 1, index = 2
            fast = fast.next
            if index > n:
                slow = slow.next
            index += 1

        slow.next = slow.next.next
        return dummy.next