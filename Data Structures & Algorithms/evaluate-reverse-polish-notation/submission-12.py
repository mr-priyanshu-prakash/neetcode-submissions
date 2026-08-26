from math import ceil,floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]  
        for t in tokens:
            if t in "+-*/":
                b,a=stack.pop(),stack.pop()
                if t =='+':
                    stack.append(a+b)
                elif t=='-':
                    stack.append(a-b)
                elif t=='*':
                    stack.append(b*a)
                else:
                    stack.append(int(a/b))
                    #di=a/b
                    #if di<0:
                       # stack.append(ceil(di))
                    #if di>0:
                       # stack.append(floor(di))
            else:
                stack.append(int(t))
        return stack[0]
                    
        