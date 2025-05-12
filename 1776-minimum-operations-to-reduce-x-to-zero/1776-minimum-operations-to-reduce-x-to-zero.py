class Solution:
    # def minOperations(self, nums: List[int], x: int) -> int:
    def minOperations(self, cards, c):
        n = len(cards)
        
        # Compute prefix sums
        prefix_sum = [0] + list(accumulate(cards))
        
        # Compute suffix sums (sum of last j elements)
        suffix_sum = [0] + list(accumulate(reversed(cards)))
        
        # Map suffix sums to the smallest j (number of elements from the end)
        suffix_map = {}
        for j in range(n + 1):
            s = suffix_sum[j]
            if s not in suffix_map:
                suffix_map[s] = j
        
        min_picks = float('inf')
        for i in range(n + 1):
            current_sum = prefix_sum[i]
            if current_sum > c:
                break
            needed = c - current_sum
            if needed in suffix_map:
                j = suffix_map[needed]
                if j <= n - i:  # Ensure no overlap between prefix and suffix
                    min_picks = min(min_picks, i + j)
        
        return min_picks if min_picks != float('inf') else -1