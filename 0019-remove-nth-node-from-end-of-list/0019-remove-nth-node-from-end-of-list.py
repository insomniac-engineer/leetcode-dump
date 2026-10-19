# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Find Node to remove
        # prev.next = prev.next.next

        # TC: O(n)
        # SC: O(1)
        if not head.next: return None

        node_to_remove, start = head, head
        length_list = 0

        while start:
            length_list += 1
            start = start.next

        for _ in range(length_list - n):
            node_to_remove = node_to_remove.next

        # IMPORTANT! DELETE HEAD edge case
        if node_to_remove == head: return head.next
        curr = head

        while curr:
            print(curr.val)
            if curr.next == node_to_remove: break
            curr = curr.next
        curr.next = curr.next.next

        return head


        