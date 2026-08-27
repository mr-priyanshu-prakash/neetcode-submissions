class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=temperatures
        res=[0]*len(temp)
        stack=[]
        for i,t in enumerate(temp):
            while stack and stack[-1][0]<t:
                stk_t,stk_i=stack.pop()
                res[stk_i]=i-stk_i
            stack.append((t,i))
        return res