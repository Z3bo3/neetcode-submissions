class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if 0 <= len(nums) <= 10**5:
            lastnum = None
            for i in sorted(nums):
                if i == lastnum:
                    return True
                else:
                    lastnum = i
        return False
        