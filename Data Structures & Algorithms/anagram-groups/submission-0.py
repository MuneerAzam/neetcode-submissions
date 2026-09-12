from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=[]
        for str in strs:
            result.append(Counter(str))
        final=[]
        i=0
        while result:
            final.append([strs.pop(0)])
            temp=result.pop(0)
            j=0
            for r in result[:]:
                if temp==r:
                    final[i].append(strs.pop(j))
                    result.pop(j)
                else:
                    j+=1
            i+=1
        return final
                