class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # All the chars from t is present in result + extra
        # TC: O(N)
        # SC: O(N)
        if len(s) < len(t): return ""

        pattern = Counter(t)
        have, need = 0, len(pattern)
        seen = defaultdict(int)
        l = 0
        best_r, best_l = 0, 0
        # Important: for senior lvl assign min_len to inf cause we haven't found one
        min_len = float("inf")
        for r in range(len(s)):
            seen[s[r]] += 1

            if seen[s[r]] == pattern[s[r]]:
                have += 1

            while have == need:
                curr_len = r - l + 1
                # Сheck if current length is less than our min
                if min_len > curr_len:
                    best_l, best_r = l, r
                    min_len = curr_len
                # Since we're moving l - decrease have value if it matches w pattern
                if s[l] in pattern and seen[s[l]] == pattern[s[l]]:
                    have -= 1
                # Decrease from seen values
                seen[s[l]] -= 1
                # Delete if the freq is 0 since key is no longer there
                if seen[s[l]] == 0:
                    del seen[s[l]]
                # Shrink
                l+= 1
        # Return slicing ONLY in result not to allocate extra memory
        return s[best_l: best_r + 1] if min_len != float("inf") else ""
