class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def add(a, b):
            return a + b
        def subtract(a, b):
            return a - b
        def multiply(a, b):
            return a * b
        def divide(a, b):
            return a // b

        stack=[]
        check={
            '+':lambda a,b:a+b,
            '-':lambda a,b:b-a,
            '*':lambda a,b:a*b,
            '/':lambda a,b:int(b/a)
            }

        for t in tokens:
            if t in check:
                a=stack.pop()
                b=stack.pop()
                stack.append(check[t](a,b))
            else:
                stack.append(int(t))
        return stack[-1]
        