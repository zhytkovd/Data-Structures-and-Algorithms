# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev, curr = None, head

        while curr: 
            nxt = curr.next # set a link to next
            curr.next = prev # set curr to previos
            prev = curr
            curr = nxt
        return prev
    
        

            

        