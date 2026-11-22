class Solution:
    def isPalindrome(self, x: int) -> bool:
        # TC: O(N)
        # SC: O(N)
        list_x = list(str(x))
        l, r = 0, len(list_x) - 1
        while l < r:
            if list_x[l] != list_x[r]:
                return False
            l += 1
            r -= 1
        return True