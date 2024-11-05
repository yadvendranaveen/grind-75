# Can be seen from examples A,A,A,B,B,B and A,A,A,B,B and A,A,A,B,B,B,C
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter_values = list(Counter(tasks).values())
        max_count = max(counter_values)
        max_freq_tasks = counter_values.count(max_count)

        slots = (max_count-1)*(n+1)+max_freq_tasks
        return max(slots, len(tasks))
        