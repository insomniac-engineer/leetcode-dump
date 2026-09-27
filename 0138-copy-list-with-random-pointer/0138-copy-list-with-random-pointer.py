"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # TC: O(N)
        # SC: O(1)
        if not head:
            return None

        old_to_new = {}
        # 1. Create copies of ALL nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # 2: Set next and random for COPIES
        curr = head
        while curr:
            # old_to_new.get(...) вернет None, если указатель равен None
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        # Return copy of new head
        return old_to_new[head]