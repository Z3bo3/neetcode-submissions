class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if 0 <= len(nums) <= 10**5 and len(nums) > 1:
            nums = sorted(nums)
            lastnum = nums[0]
            for i in nums[1:]:
                if i == lastnum:
                    return True
                else:
                    lastnum = i
        return False
        