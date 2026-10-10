class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the start of sequence
        nums_set = set()
        for i in nums:
            nums_set.add(i)

        counter_max = 0

        for i in nums_set:
            if i - 1 not in nums_set:
                temp = 1
                j = i
                while j + 1 in nums_set:
                    temp += 1
                    j += 1
                counter_max = max(counter_max, temp)
        return counter_max