class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-v for v in stones]
        heapify(stones)
        while len(stones)>1:
            stone1, stone2 = heappop(stones), heappop(stones)
            newval = abs(stone1-stone2)
            if newval==0:
                continue
            heappush(stones, -newval)
        return -stones[0] if stones else 0
