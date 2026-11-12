# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = {}

        curr = head
        count = 0
        while curr:
            if curr in node_set:
                return True
            else:
                node_set[curr] = 0
            curr = curr.next
        return False
        