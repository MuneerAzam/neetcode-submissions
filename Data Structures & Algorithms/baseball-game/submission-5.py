def op(o,arr,i):
        if o=='+':
            arr.append(arr[i[0]-2]+arr[i[0]-1])
            i[0]+=1
        elif o=='D':
            arr.append(arr[i[0]-1]*2)
            i[0]+=1
        elif o=='C':
            arr.pop()
            i[0]-=1
        else:
            arr.append(int(o))
            i[0]+=1
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        i=[0]
        for o in operations:
            op(o,res,i)
            print(res)
        return sum(res)
        