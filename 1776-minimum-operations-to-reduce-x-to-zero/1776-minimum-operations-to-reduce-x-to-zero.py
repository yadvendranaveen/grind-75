class Solution:
    # def minOperations(self, nums: List[int], x: int) -> int:
    def minOperations(self, cards, target):

        """
        Find minimum number of card picks needed to eat exactly target candies.
        Cards can only be picked from either end of the array.
        
        Args:
            cards: List of integers representing candy values on each card
            target: Total number of candies Alice needs to eat
        
        Returns:
            Minimum number of cards needed, or -1 if impossible
        """
        n = len(cards)
        if n == 0:
            return 0 if target == 0 else -1
        
        total = sum(cards)
        
        # If target is greater than total, it's impossible
        if target > total:
            return -1
            
        # If we need to eat all candies, pick all cards
        if target == total:
            return n
        
        # We need to find a subarray with sum (total - target) that we can leave behind
        # The cards we pick must be from both ends, so the subarray we leave must be contiguous
        
        remaining = total - target
        min_picks = float('inf')
        
        # Calculate prefix sums for efficient subarray sum computation
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + cards[i]
        
        # For each possible starting position of the "left behind" subarray
        for start in range(n):
            # Binary search to find the end position
            left, right = start, n - 1
            
            # Exact match with binary search
            while left <= right:
                mid = (left + right) // 2
                subarray_sum = prefix_sum[mid + 1] - prefix_sum[start]
                
                if subarray_sum == remaining:
                    # We found a valid subarray to leave behind
                    # Cards picked = all cards - cards left behind
                    picks = n - (mid - start + 1)
                    min_picks = min(min_picks, picks)
                    break
                elif subarray_sum < remaining:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return min_picks if min_picks != float('inf') else -1