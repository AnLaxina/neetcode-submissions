import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}
        for num in nums:
            freq_count[num] = 1 + freq_count.get(num, 0)
        
        heap = []

        for num, count in freq_count.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for tupl in heap:
            result.append(tupl[1])
        
        return result
