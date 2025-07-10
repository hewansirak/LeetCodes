# Last updated: 7/10/2025, 10:14:21 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        ans = ListNode()
        aux = ans

        for i in range(len(lists)):
            if lists[i]: heapq.heappush(heap, (lists[i].val, i))

        while heap:
            val, i = heapq.heappop(heap)
            aux.next = ListNode(val)
            aux = aux.next
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))
        return ans.next