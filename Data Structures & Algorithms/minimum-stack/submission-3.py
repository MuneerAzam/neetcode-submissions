import heapq
class MinStack:

    def __init__(self):
        self.list=[]
        return

    def push(self, val: int) -> None:
        if not self.list:
            self.list.append((val,val))
        else:
            self.list.append((val,min(self.list[-1][1],val)))
        return

    def pop(self) -> None:
        a=self.list.pop()
        return

    def top(self) -> int:
        return self.list[-1][0]

    def getMin(self) -> int:
        return self.list[-1][1]