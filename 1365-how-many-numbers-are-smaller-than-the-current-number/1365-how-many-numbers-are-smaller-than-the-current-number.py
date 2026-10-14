class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        # SC: O(n)
        # TC: O(nlogn) sorting
        
        # Another way O(N) is to count frequencies of 102 values, kinda overkill
        sorted_val_index = {}

        for idx, val in enumerate(sorted(nums)):
            if val not in sorted_val_index: # duplicate
                sorted_val_index[val] = idx
        # for each value in nums return index
        return [sorted_val_index[val] for val in nums]
        # res = list()

        # for i in nums:
        #     print(i)
        #     res.append(sorted_val_index[i])
        # return res