class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = Counter(s1)
        seen = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            # [e] -> 1
            seen[s2[r]] += 1

            while (r - l + 1) > len(s1):
                seen[s2[l]] -= 1

                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l += 1
            
            if pattern == seen:
                return True
        return False
        