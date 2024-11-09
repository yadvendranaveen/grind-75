class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.timemap[key], timestamp, key=lambda x:x[0])-1    
        return self.timemap[key][idx][1] if idx>=0 else ''

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)