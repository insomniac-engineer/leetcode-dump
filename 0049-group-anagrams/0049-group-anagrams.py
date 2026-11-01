class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # TC: O(N * k)
        # SC: O(N) - because we don't copy/create string. we just put their ref in
        # in anagrams freq of characters are the same
        # e.g. eat: 'e' -> 1 'a' -> 1 't' -> 1

        # (0, 0, 0, 0, 0, ...)
        # (1, 0, 0, 0, 0, ...) 'a'

        anagrams_dict = defaultdict(list)

        for s in strs:
            freq_chars = [0] * 26
            for ch in s:
                pos = ord(ch) - ord('a')
                freq_chars[pos] += 1
            freq_chars_tuple = tuple(freq_chars)
            anagrams_dict[freq_chars_tuple].append(s)
        return list(anagrams_dict.values())