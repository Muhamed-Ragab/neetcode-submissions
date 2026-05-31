class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_set = {}
        for index, num in enumerate(nums):
            if num in my_set:
                return [my_set[num], index]
            else:
                my_set[target - num] = index
        return []
        