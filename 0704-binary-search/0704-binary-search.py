class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # TC: O(logN)
        # SC: O(1)
        l, r = 0, len(nums)
        
        while l < r:
            mid = (l + r)  // 2
            print(f'l = {l}, r = {r}, mid = {mid}')
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else: return mid
        return -1