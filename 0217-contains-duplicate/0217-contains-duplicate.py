class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique_numbers = set()

        for n in nums:
            if n in unique_numbers:
                return True
            unique_numbers.add(n)
        return False