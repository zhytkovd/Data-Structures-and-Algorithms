# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle
        middle, fast = head, head

        while fast.next and fast.next.next:
            middle = middle.next
            fast = fast.next.next

        second = middle.next
        middle.next = None

        # reverse middle list
        prev, curr = None, second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # merge both lists together
        curr1 = head
        curr2 = prev
        while curr2:
            nxt = curr1.next
            nxt2 = curr2.next
            curr1.next = curr2
            curr2.next = nxt
            curr1 = nxt
            curr2 = nxt2
        
        