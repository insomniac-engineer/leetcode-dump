# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS - recursive
        if not root: return None
        # print(root.val)
        # print(root.left.val)
        # print(root.right.val)
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.right)
        # self.invertTree(root.left)

        # BFS - level by level using queue
        # 1. add root to (de)queue
        # 2. pop node fro queue and swap left with right
        # 3. add children if any
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root