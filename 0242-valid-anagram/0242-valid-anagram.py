class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
        dict_s = defaultdict(int)

        for char_s in s:
            dict_s[char_s] += 1
        
        for char_t in t:
            if char_t not in dict_s:
                return False
            dict_s[char_t] -= 1
            if dict_s[char_t] < 0:
                return False
            if dict_s[char_t] == 0:
                del dict_s[char_t]
        return len(dict_s) == 0  