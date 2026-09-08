class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # Monotonic stack stores the indexes

        stack = [] # only indexes there
        res = [0] * len(temperatures)
        for idx_t, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = idx_t - prev_index
            stack.append(idx_t)
        return res