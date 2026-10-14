class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # dict [val] -> index
        # iterate through nums and check if the val is alr in dict
        # if the val is in dict - we found the duplicate

        index_val = defaultdict(int)

        for idx, val in enumerate(nums):
            if val in index_val:
                if abs(idx - index_val[val]) <= k:
                    return True
            index_val[val] = idx
        return False