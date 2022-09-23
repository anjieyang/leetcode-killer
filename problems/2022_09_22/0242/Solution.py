class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCountMap = self.getCountMap(s)
        tCountMap = self.getCountMap(t)

        return sCountMap == tCountMap

    def getCountMap(self, string):
        countMap = {}
        for i in string:
            if i not in countMap.keys():
                countMap[i] = 1
            else:
                countMap[i] += 1

        return countMap
