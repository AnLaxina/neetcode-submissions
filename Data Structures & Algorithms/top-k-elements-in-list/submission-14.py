import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = nums.count(num)
        
        heap = []

        for num, count in count.items():
            heapq.heappush(heap, (count, num))
            print(num, count)
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result

        