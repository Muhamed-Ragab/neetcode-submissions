class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for str in strs:
            sorted_str = "".join(sorted(str))
            my_dict[sorted_str].append(str)
        return list(my_dict.values())