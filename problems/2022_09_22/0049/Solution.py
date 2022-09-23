class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for i in strs:
            key = ''.join(sorted(i))
            if key not in res.keys():
                res[key] = [i]
            else:
                res[key].append(i)

        return [val for val in res.values()]
