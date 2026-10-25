class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        value_index = dict()
        i = 0

        while i < len(nums):
            if nums[i] in value_index and abs(i - value_index[nums[i]]) <= k:
                return True
            value_index[nums[i]] = i
            i += 1
        return False