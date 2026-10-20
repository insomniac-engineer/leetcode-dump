# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head.next and n == 1: return None
        # Remove means node will point on node k + 1
        # curr.next = curr.next.next

        s, f = head, head
        # Slow pointer will start n times late
        # It will point on element to remove
        for _ in range(n):
            f = f.next #3
        
        while f:
            s = s.next
            f = f.next 
        
        curr = head

        # Edge case: if we move head
        if s == head: return head.next

        while curr.next != s:
            curr = curr.next
        
        curr.next = curr.next.next
        return head