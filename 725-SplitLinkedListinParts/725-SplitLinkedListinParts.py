# Last updated: 5/20/2025, 10:18:20 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # size = figure out the number of nodes
        # patition_size = size // k
        # rm = size % k

        # size = figure out the number of nodes
        size = 0
        curr = head

        while curr:
            size += 1
            curr = curr.next

        partition_size = size // k
        rm = size % k
        ans = []
        curr = head

        for _ in range(k):
            dummy = ListNode()
            partition = dummy
            curr_par_size = partition_size
            if rm > 0:
                rm -= 1
                curr_par_size += 1

            for _ in range(curr_par_size):
                partition.next = ListNode(curr.val)
                partition = partition.next
                curr = curr.next
            
            ans.append(dummy.next)

        return ans