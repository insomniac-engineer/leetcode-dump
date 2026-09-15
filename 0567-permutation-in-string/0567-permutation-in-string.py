class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Time Complexity: O(n * 26)
        # Space Complexity: O(1)
        # permutation -> the count must be equal, values can be shuffled (order matters)
        pattern = Counter(s1) # [a] -> 1 [b] -> 2
        l = 0
        current_window = defaultdict(int)
        len_s1 = len(s1)
        for r in range(len(s2)):
            current_window[s2[r]] += 1 # e -> 1

            if r - l + 1 > len_s1:
                current_window[s2[l]] -= 1
                if current_window[s2[l]] <= 0:
                    del current_window[s2[l]]
                l += 1

            # We are comparing n times 26 ASCII symbols (characters)
            if current_window and current_window == pattern: return True
            
        return False