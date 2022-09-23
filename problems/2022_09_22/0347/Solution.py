class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for i in nums:
            if i in countMap.keys():
                countMap[i] += 1
            else:
                countMap[i] = 1

        countTuple = list(countMap.items())
        countTuple.sort(key=lambda x: -x[1])

        count = 0
        res = []
        while count < k and count < len(countTuple):
            res.append(countTuple[count][0])
            count += 1

        return res
