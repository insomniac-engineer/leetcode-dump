# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # 1 -> null (tmp = 2)
        # 2 -> 1 -> null (tmp = 3)
        # 3 -> 2 -> 1 -> null (tmp = 4)
        prev, tmp = None, None
        curr = head
        while curr:
            tmp = curr.next # 2
            curr.next = prev # 1 -> None
            
            prev = curr # 1
            curr = tmp
        return prev


