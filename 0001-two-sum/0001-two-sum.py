class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # TC: O(N)
        # SC: O(N)
        # number -> index
        # if target - current_number alr in dict -> we found a pair

        nums_dict = defaultdict(int)

        for idx, n in enumerate(nums):
            if target - n in nums_dict:
                return [idx, nums_dict[target - n]]
            nums_dict[n] = idx
        return []

        