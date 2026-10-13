class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # # TC: 0(nlogn)
        # # SC: O(1)
        # nums.sort()

        # for i in range(0, len(nums)):
        #     if nums[i] != i: return i
        # # [0, n], last element should be n
        # return len(nums)

        #range is exclusive for last element
        #TC: O(n)
        #SC: O(1)
        expected_sum = sum(range(len(nums) + 1))
        actual_sum = sum(nums)
        return expected_sum - actual_sum