class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '[':
                stack.append(']')
            elif  s[i] == '{':
                stack.append('}')
            elif  s[i] == '(':
                stack.append(')')
            else:
                if len(stack) == 0 or s[i] != stack.pop():
                    return False
            i += 1
        return len(stack) == 0