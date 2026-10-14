class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # 1 2 2 3 8
        # can't just return idx + 1 bc we have duplicates for "2"
        # [1] -> 0
        # [2] -> 1

        sorted_val_index = {}
        
        sorted_nums = sorted(nums)

        for idx, val in enumerate(sorted_nums):
            if val in sorted_val_index: # duplicate
                continue
            sorted_val_index[val] = idx

        res = list()

        for i in nums:
            print(i)
            res.append(sorted_val_index[i])
        return res