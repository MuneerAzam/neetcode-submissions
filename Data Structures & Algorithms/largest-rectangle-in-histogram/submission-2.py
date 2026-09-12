class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxa=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                pi,ph=stack.pop()
                maxa=max(maxa,ph*(i-pi))
                start=pi
            stack.append((start,h))
        for i,h in stack:
            maxa=max(maxa,h*(len(heights)-i))
        return maxa