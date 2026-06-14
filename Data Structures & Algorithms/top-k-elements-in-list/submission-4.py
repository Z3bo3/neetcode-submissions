class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictres = {}
        listresult = []
        for i in nums:
            if i not in dictres:
                dictres[i] = 1
            elif i in dictres:
                dictres[i] = dictres[i] + 1
        sorted_dictres = sorted(dictres.items(),key=lambda item: int(item[1]), reverse=True)
        print(sorted_dictres)
        for i in range(k):
            listresult.append(sorted_dictres[i][0])
        return listresult