class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1=[0]*130
        count2=[0]*130
        for i in s:
            count1[ord(i)]+=1
        for i in t:
            count2[ord(i)]+=1
        return count1==count2
