class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.curr=0
        self.dict={}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.val=self.dict.pop(key)
        self.dict[key]=self.val
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if self.curr==self.cap:
            if key not in self.dict:
                self.dict.pop(next(iter(self.dict)))
                self.dict[key]=value
            else:
                self.val=self.dict.pop(key)
                self.dict[key]=self.val
                self.dict[key]=value
        else:
            if key not in self.dict:
                self.curr+=1
            self.dict[key]=value
