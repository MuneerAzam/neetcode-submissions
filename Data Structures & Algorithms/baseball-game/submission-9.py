class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr=[]
        for o in operations:
            if o=='+':
                arr.append(arr[-2]+arr[-1])
            elif o=='D':
                arr.append(arr[-1]*2)
            elif o=='C':
                arr.pop()
            else:
                arr.append(int(o))
        return sum(arr)