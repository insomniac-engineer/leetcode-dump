class MinStack:
    # One list to store values (push/pop/top)
    # Another list to maintain top element on each iteration
    
    # 1 2 0 stack
    # 1 2 2 sync_stack

    # Space Complexity: O(n)
    def __init__(self):
        self.stack = []
        self.sync_stack = []
    # O(1)
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.sync_stack or self.sync_stack[-1] > val:
            self.sync_stack.append(val)
        else:
            self.sync_stack.append(self.sync_stack[-1])
    # O(1)
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.sync_stack.pop()
    # O(1)
    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        
    # O(1)
    def getMin(self) -> int:
        return self.sync_stack[-1] if self.stack else None