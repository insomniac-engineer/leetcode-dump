# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return
        """
        Do not return anything, modify head in-place instead.
        """
        # TC: O(N)
        # SC: O(1)

        # 1. Slow & Fast pointer to find half of the list

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. IMPORTANT: divide list into half and reverse SECOND half
        second = slow.next # 4->5
        slow.next = None # 1->2->3->None

        prev = None
        curr = second

        while curr:
            nxt = curr.next #4 5
            curr.next = prev # 4->3 -> None

            prev = curr # 3
            curr = nxt # 4

        # 3. Match head with tail

        while head and prev:
            tmp1 = head.next
            tmp2 = prev.next

            head.next = prev
            prev.next = tmp1

            head = tmp1
            prev = tmp2