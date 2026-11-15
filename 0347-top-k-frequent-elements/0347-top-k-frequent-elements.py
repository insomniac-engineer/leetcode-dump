class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 -> 1
        # 2 -> 2
        # 3 -> 3

        freq_map = Counter(nums)
        heap = []

        for val, freq in freq_map.items():
            heapq.heappush(heap, (freq, val))
            while len(heap) > k:
                heapq.heappop(heap)
        return [val for freq, val in heap]
        print(heap)