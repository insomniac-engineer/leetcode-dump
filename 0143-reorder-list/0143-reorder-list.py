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

        # Calculate length of linked list
        list_len = 0
        curr = head

        while curr:
            list_len += 1
            curr = curr.next
        half_len = list_len // 2 #first part is smaller

        p2 = head

        # divide into 2 parts
        for _ in range(half_len):
            p2 = p2.next

        p1 = head

        # cut connection to the second part
        while p1.next != p2:
            p1 = p1.next

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

        if tail:
            start = head
            while start.next:
                start = start.next
            start.next = tail