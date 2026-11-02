import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TC: O(N + U * log(k+1))
        # SC: O(U + k)
        # nums = [1,2,2,3,3,3] k = 2

        # 1. initialize val_freq dict 
        # 2. initialize min_heap (balanced binary tree)
        # 3. we use min heap because root is always the least frequency. once len(min_heap) > k -> pop element (it's always least used one)

        val_freq = defaultdict(int)

        for n in nums:
            val_freq[n] += 1
        min_heap = []

        for val,freq in val_freq.items():
            heapq.heappush(min_heap,(freq, val)) # we push first otherwise we might pop not the most freq element and then add less frequent one
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        res = [val for _, val in min_heap]
        return res