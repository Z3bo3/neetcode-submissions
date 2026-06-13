class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums and len(nums) > 1:
            for i in range(1, len(nums), 3):
                if target == nums[i]:
                    return i
                elif target == nums[i - 1]:
                    return i - 1
                elif target == nums[i + 1]:
                    return i + 1
        elif target in nums and len(nums) == 1:
            return 0
        return -1
        