class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    # Step 1: Combine start time, end time, and profit into a list of jobs and sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

    # Step 2: Initialize DP array with a tuple (end time, profit)
        dp = [(0, 0)]  # Initial DP array, starting with zero profit at time 0

    # Step 3: Iterate over each job
        for s, e, p in jobs:
            # Use binary search to find the latest non-overlapping job
            i = bisect_right(dp, (s, math.inf)) - 1
            current_profit = dp[i][1] + p
            if current_profit > dp[-1][1]:
                dp.append((e, current_profit))

        # The answer is the maximum profit at the end of all jobs
        return dp[-1][1]
