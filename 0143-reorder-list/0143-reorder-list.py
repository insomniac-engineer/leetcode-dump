# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # TC: O(n)
        # SC: O(1)

        # Requires 3 algo:
        # divide linked list into 2 parts (find length first)
        # reverse the second part (first part.next = None)
        # match zigzag

        if not head or not head.next:
            return

        p1, p2 = head, head

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        p2 = p1.next
        p1.next = None

        # reverse
        curr, prev = p2, None
        while curr:
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        tail = prev
        # [0,1,2,3]
        # [6 5 4]

        start = head
        # 0 -> 6 -> 1 (ZIGZAG)
        while tail and start:
            temp_tail = tail.next
            temp_start = start.next

            start.next = tail # 0->6
            tail.next = temp_start # 0->6->1
            tail = temp_tail
            start = temp_start