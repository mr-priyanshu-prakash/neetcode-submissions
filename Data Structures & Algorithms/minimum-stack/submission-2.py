class MinStack:

    def __init__(self):
        self.stk=[]
        self.minst=[]
    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minst:
            self.minst.append(val)
        elif self.minst[-1]<val:
            self.minst.append(self.minst[-1])
        else:
            self.minst.append(val)
    def pop(self) -> None:
        self.stk.pop()
        self.minst.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minst[-1]
        
