class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TC: O(N^2) (ONlogN)
        # SC: O(N)
        nums.sort()
        res = set() 
        idx_n = 0
        # [-1,0,1,2,-1,-4]
        # [ -4 -1 -1 0 1 2]
        while idx_n < len(nums) - 2:
            l, r = idx_n + 1, len(nums) - 1
            add1 = nums[idx_n]
            while l < r:
                if add1 + nums[l] + nums[r] > 0:
                    r -= 1
                elif add1 + nums[l] + nums[r] < 0:
                    l += 1
                else: # equal to 0
                    res.add((add1, nums[l], nums[r]))
                    r -= 1
                    l += 1
            idx_n += 1
            l = idx_n + 1
            r = len(nums) - 1
        return [list(triplet) for triplet in res]