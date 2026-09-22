class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # All the chars from t is present in result + extra
        # TC: O(N)
        # SC: O(N)
        if len(s) < len(t): return ""

        final_res = ""
        pattern = Counter(t)
        have, need = 0, len(pattern)
        seen = defaultdict(int)
        l = 0
        best_r, best_l = len(s) - 1, 0
        min_len = float("inf")
        for r in range(len(s)):
            seen[s[r]] += 1

            if seen[s[r]] == pattern[s[r]]:
                have += 1

            while have == need:
                min_len = r - l + 1
                if min_len < best_r - best_l + 1:
                    best_l, best_r = l, r
                if s[l] in pattern and seen[s[l]] == pattern[s[l]]:
                    have -= 1
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l+= 1
        return s[best_l: best_r + 1] if min_len != float("inf") else ""