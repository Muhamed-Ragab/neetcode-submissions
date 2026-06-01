class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        result = []

        for index in range(0, len(nums) - 1):
            prefix.append(prefix[index] * nums[index])

        for index in range(len(nums) - 1, 0, -1):
            suffix.insert(0, suffix[0] * nums[index])

        for index in range(0, len(nums)):
            result.append(prefix[index] * suffix[index])

        return result