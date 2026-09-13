class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        str=''.join(char.lower() for char in s if char.isalnum())
        l=len(str)
        j=len(str)-1
        while i<j:
            if(str[i]!=str[j]):
                return False
            i+=1
            j-=1
        return True