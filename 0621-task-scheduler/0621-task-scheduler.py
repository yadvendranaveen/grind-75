class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        pq = list(map(lambda x: -x, Counter(tasks).values()))
        heapify(pq)

        time = 0
        while pq:

            cycle, task_count, stack = n+1, 0, []
            while cycle>0 and pq:
                freq = -heappop(pq)
                if freq>1:
                    stack.append( -(freq-1) )
                cycle-=1
                task_count+=1

            pq = list(heapq.merge(pq, stack))
            time += task_count if not pq else n+1 #add time taken for complete cycle if we expect tasks in next cycle, ie, pq not empty
        return time
            
                
