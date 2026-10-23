# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # TC: O(N)
        # SC: O(1)
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        # 7 + 8 = 15 we carry 1

        # 3 2 7
        # 2 1 5
        # -----
        # 2 4 5

        # 7 2 3
        # 5 1 2
        # -----
        # 2 4 5

        while l1 or l2 or carry:
            add1 = l1.val if l1 else 0
            add2 = l2.val if l2 else 0

            val = add1 + add2 + carry

            node_val = val % 10
            carry = val // 10

            curr.next = ListNode(node_val)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next