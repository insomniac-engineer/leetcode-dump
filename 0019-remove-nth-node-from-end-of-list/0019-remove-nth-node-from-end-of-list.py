# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find len of entire list of nodes
        # len(nodes) - n is the node we need to remove
        # keep ref of prev node to link with next one (instead of deleted)
        # return head

        # TC: O(N)
        # SC: O(1)
        if n == 1 and head.next == None: return None

        res = head
        tmp = head
        len_list = 0

        while res:
            len_list += 1
            res = res.next
        i = 0
        prev = None
        idx = len_list - n
        # Edge case if we delete first element in list
        if idx == 0:
            return head.next
        # Keep prev element and link it with removed-to next one
        while tmp:
            if idx == i:
                tmp_next = tmp.next
                prev.next = tmp_next
                break
            prev = tmp
            tmp = tmp.next
            i += 1
        return head