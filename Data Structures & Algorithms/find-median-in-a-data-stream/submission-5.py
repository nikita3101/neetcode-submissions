class MedianFinder:
    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.minheap, self.maxheap = [], []

    def addNum(self, num: int) -> None:
        if (len(self.maxheap) == 0 or num <= -1 * self.maxheap[0]):
            heapq.heappush(self.maxheap, -1 * num)
        else: 
            heapq.heappush(self.minheap, num)
        if (len(self.maxheap) > len(self.minheap)+1):
            heapq.heappush(self.minheap, -1 * self.maxheap[0])
            heapq.heappop(self.maxheap)
        elif ((len(self.minheap) > len(self.maxheap)+1)):
            heapq.heappush(self.maxheap, -1 * self.minheap[0])
            heapq.heappop(self.minheap)


    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        elif len(self.minheap) < len(self.maxheap):
            return -1 * self.maxheap[0]
        else:
            return (self.minheap[0] + (-1* self.maxheap[0]) ) / 2
            
        
        