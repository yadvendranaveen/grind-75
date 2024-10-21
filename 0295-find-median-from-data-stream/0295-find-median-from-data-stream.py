class MedianFinder:

    def __init__(self):
        self.l = []
        self.r = []
        self.isOdd = False

    def addNum(self, num: int) -> None:
        self.isOdd = not self.isOdd
        heappush(self.r, num)
        heappush(self.l, -heappop(self.r))
        if self.isOdd:
            heappush(self.r, -heappop(self.l))

    def findMedian(self) -> float:
        return self.r[0] if self.isOdd else (-self.l[0]+self.r[0])/2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#[null,null,-1.00000,null,-1.50000,null,-2.00000,null,-2.50000,null,-3.00000]