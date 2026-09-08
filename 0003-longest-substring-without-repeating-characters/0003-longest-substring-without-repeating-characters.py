class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        l = 0
        uniq = set()
        max_res = 0
        for r in range(len(s)):
            while s[r] in uniq:
                uniq.remove(s[l])
                l += 1
            uniq.add(s[r])
            max_res = max(max_res, r - l + 1)
        return max_res