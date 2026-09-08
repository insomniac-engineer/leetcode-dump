class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # We need at least 2 integers and 1 operator to perform operation

        # Once we have operator - we can perform operation, 
        # In this case '+' is not a digit, we do 1 + 2
        # +
        # 1
        # 2

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        stack = []
        res = 0
        for t in tokens:
            # IMPORTANT: -3 is not a digit in python, 3 is
            if t.lstrip("-").isdigit():
                stack.append(int(t))
            else:
                if t == "+":
                    res = stack.pop() + stack.pop()
                # IMPORTANT: for - and / order plays role
                elif t == "-":
                    temp = stack.pop()
                    res = stack.pop() - temp
                elif t == "*":
                    res = stack.pop() * stack.pop()
                elif t == "/":
                    temp = stack.pop()
                    res = stack.pop() / temp
                stack.append(int(res))
        return stack[-1]
        


        