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
        # SC: O(1)
        orig_to_copy = dict()

        curr = head
        curr2 = head
        dummy = Node(0)
        start = dummy
        res = dummy
        while curr:
            orig_to_copy[curr] = Node(curr.val)
            #print(orig_to_copy[curr].val)
            curr = curr.next
        # [orig 7-> copy 7]
        
        for orig, duplicate in orig_to_copy.items():
            dummy.next = duplicate
            dummy = dummy.next

        start = start.next

        for orig, duplicate in orig_to_copy.items():
            if orig.random == None:
                start.random  = None
            else:
                start.random = orig_to_copy[orig.random]
            start = start.next
        return res.next