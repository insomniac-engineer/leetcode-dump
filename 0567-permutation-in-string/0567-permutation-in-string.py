class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time Complexity: O(n * 26)
        # Space Complexity: O(1)
        # permutation -> the count must be equal, values can be shuffled (order matters)
        pattern = Counter(s1) # [a] -> 1 [b] -> 2
        l = 0
        seen = defaultdict(int)
        len_s1 = len(s1)
        for r in range(len(s2)):
            seen[s2[r]] += 1 # e -> 1

            if r - l + 1 > len_s1:
                seen[s2[l]] -= 1
                if seen[s2[l]] <= 0:
                    del seen[s2[l]]
                l += 1

            # We are comparing n times 26 ASCII symbols (characters)
            if seen == pattern: return True
            
        return False