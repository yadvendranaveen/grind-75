class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        def upper_bound():
            l,r = 0, len(arr)
            while l<r:
                mid = (l+r)//2
                if arr[mid][0]<=timestamp:
                    l = mid+1
                else:
                    r = mid
            return l
        idx = upper_bound() 
        return arr[idx-1][1] if idx else ""
        # idx = bisect.bisect(self.store[key], timestamp, key=lambda x:x[0])
        # return self.store[key][idx-1][1] if idx else ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)