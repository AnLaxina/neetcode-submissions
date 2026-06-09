import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)
        
        # Make a min heap and put the (frequency, number) as values
        heap = []

        for num, count in count_dict.items():
            heapq.heappush(heap, (count, num))
            # To avoid adding excess, if the heap's length exceeds k, just pop it
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Add the result in from the heap
        result = []

        for tup in heap:
            result.append(tup[1])

        return result
        