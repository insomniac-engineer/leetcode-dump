class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # TC: O(logN)
        # SC: O(1)

        l,r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                return mid
        return - 1