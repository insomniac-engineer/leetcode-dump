class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation - chars frequencies are the same

        pattern = Counter(s1)

        seen = defaultdict(int)
        l = 0
        # Count +1 only when ALL the frequencies match
        need, have = len(pattern), 0
        for r in range(len(s2)):

            seen[s2[r]] += 1
            if seen[s2[r]] == pattern[s2[r]]:
                have += 1
            while r - l + 1 > len(s1):
                if seen[s2[l]] == pattern[s2[l]]:
                    have -= 1
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l += 1
            
            if have == need:
                return True
        return False