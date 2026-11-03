class Solution:
    def maxArea(self, height: list[int]) -> int:
        # SC: O(1)
        # TC: O(N)
        l, r = 0, len(height) - 1
        res, h = 0, 0

        while l < r:
            h = min(height[l], height[r])
            width = r - l
            res = max(res, h * width)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res