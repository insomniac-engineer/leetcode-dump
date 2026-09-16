class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation -> we care about chars frequency (dict)

        pattern = Counter(s1)
        seen = defaultdict(int)
        len_s1 = len(s1)
        l = 0
        need, have = len(pattern), 0
        for r in range(len(s2)):
            seen[s2[r]] += 1
            # match happens only if we have enough frequency (from need) for each key
            if pattern[s2[r]] == seen[s2[r]]:
                have += 1
            while r - l + 1 > len_s1:
                if pattern[s2[l]] == seen[s2[l]]:
                    have -= 1
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l += 1
            # # takes O(n * 26)
            # if pattern == seen:
            #     return True
            # instead of comparing entire dict we compare counters
            if have == need:
                return True
        return False

        