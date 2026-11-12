# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # count the size of the list
        if head.next == None: return None
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        curr = head
        
        for i in range(count-n-1):
            curr = curr.next
            
        if n == count:
            head = head.next

        if not curr.next.next:
            curr.next = None
        else:
            curr.next = curr.next.next
        return head