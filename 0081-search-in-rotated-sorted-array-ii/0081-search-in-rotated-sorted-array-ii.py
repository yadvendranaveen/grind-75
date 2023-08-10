class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if target in Counter(nums):
            return True
        return False
        