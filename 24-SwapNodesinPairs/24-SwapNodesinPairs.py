# Last updated: 6/11/2025, 11:26:09 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head

        prev = None 
        cur = head
        ans = head.next

        while cur and cur.next:
            adj = cur.next
            if prev: prev.next = adj

            cur.next, adj.next = adj.next, cur
            prev = cur
            cur = cur.next

        return ans or head   