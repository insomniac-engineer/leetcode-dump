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
        # TC: O(n)
        # SC: O(n)
        orig_to_copy = dict()

        curr = head

        while curr:
            orig_to_copy[curr] = Node(curr.val)
            curr = curr.next
        
        for orig, duplicate in orig_to_copy.items():
            duplicate.next = orig_to_copy.get(orig.next)
            duplicate.random = orig_to_copy.get(orig.random)

        return orig_to_copy.get(head)