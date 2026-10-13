class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # 0 1 3

        # if index != val -> return val
        # TC: 0(nlogn)
        # SC: O(1)
        nums.sort()

        for i in range(0, len(nums)):
            if nums[i] != i: return i
            if i == len(nums) - 1: return len(nums)
        return -1