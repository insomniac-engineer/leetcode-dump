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
        # Step 1: create original to copy dict [orig_node] -> copy_node
        # Step 2: iterate over dict, and for each value (copy) set next and rndm
        orig_to_copy = dict()

        dummy = head

        while dummy:
            orig_to_copy[dummy] = Node(dummy.val)
            dummy = dummy.next
        
        #print(orig_to_copy)

        for orig, copy in orig_to_copy.items():
            copy.next = orig_to_copy.get(orig.next)
            copy.random = orig_to_copy.get(orig.random)
        return orig_to_copy.get(head)