class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if len(s1) > len(s2):
            return False
        freq_map = defaultdict(int)
        l = 0
        pattern_map = Counter(s1)
        need, have = len(pattern_map), 0
        for r in range(len(s2)):
            freq_map[s2[r]] += 1
            if freq_map[s2[r]] == pattern_map[s2[r]]:
                have += 1

            while r - l + 1 > len(s1):
                if freq_map[s2[l]] == pattern_map[s2[l]]:
                    have -= 1
                freq_map[s2[l]] -= 1
                if freq_map[s2[l]] == 0:
                    del freq_map[s2[l]]
                l += 1

            if need == have:
                return True
            # It requires O(26*n) in the worst case
            # if pattern_map == freq_map:
            #     return True
        return False