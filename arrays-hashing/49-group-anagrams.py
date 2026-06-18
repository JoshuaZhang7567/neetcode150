from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}

        for string in strs:

            sort = ''.join(sorted(string))

            if sort not in anagramDict:
                anagramDict[sort] = []
            anagramDict[sort].append(string)

        return list(anagramDict.values())