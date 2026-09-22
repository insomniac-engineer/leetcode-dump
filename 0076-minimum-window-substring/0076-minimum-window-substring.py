class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # All the chars from t is present in result + extra
        if len(s) < len(t): return ""
        final_res = ""
        pattern = Counter(t)
        have, need = 0, len(pattern)
        seen = defaultdict(int)
        l = 0
        for r in range(len(s)):
            seen[s[r]] += 1

            if seen[s[r]] == pattern[s[r]]:
                have += 1

            while have == need:
                if final_res == "":
                    final_res = s[l:r+1]
                else:         
                    if len(final_res) >= len(s[l:r+1]):
                        final_res = s[l:r+1]
                if s[l] in pattern and seen[s[l]] == pattern[s[l]]:
                    have -= 1
                seen[s[l]] -= 1
                if seen[s[l]] == 0:
                    del seen[s[l]]
                l+= 1
        return final_res