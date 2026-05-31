class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_items = Counter(nums).most_common(k)
        return [num for num, count in sorted_items]