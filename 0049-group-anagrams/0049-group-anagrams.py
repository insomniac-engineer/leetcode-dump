class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # TC: O(N * k)
        # SC: O(N), we put references of each string to dict
        freq_counter = [0] * 26
        pattern_words = defaultdict(list)
        for s in strs:
            freq_counter = [0] * 26
            for ch in s:
                freq_counter[ord(ch) - ord('a')] += 1
            pattern_words[tuple(freq_counter)].append(s)
        return list(pattern_words.values())