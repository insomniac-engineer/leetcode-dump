class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # replace the least common char in sliding window
        # while total - counter(most_common_val) > k
        char_count = defaultdict(int)
        l = 0
        max_count, max_len = 0, 0

        for r in range(len(s)):
            # [A] -> 3
            char_count[s[r]] += 1

            max_count = max(max_count, char_count[s[r]])

            while (r - l + 1) - max_count > k:
                char_count[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
        return max_len