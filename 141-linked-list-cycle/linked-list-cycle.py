# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_set = {}
        curr, nxt = head, head

        count = 0
        while (curr != None) and (nxt != None):
            if nxt.next == None or curr == None: return False
            
            if not nxt.next.next:
                return False
            else:
                nxt = nxt.next.next

            curr = curr.next
            if curr == nxt: return True


        return False
        