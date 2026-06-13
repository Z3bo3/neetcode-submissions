class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevnums = []
        if 0 <= len(nums) <= 10**5:
            for i in nums:
                if i in prevnums:
                    return True
                else:
                    prevnums.append(i)
        return False
        