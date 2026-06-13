class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        if 0 <= len(nums) <= 10**5:
            for i in sorted(nums):
                if i in hashset:
                    return True
                else:
                    hashset.add(i)
        return False
        