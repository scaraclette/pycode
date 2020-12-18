class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.minItems = []
        

    def push(self, x: int) -> None:
        self.items.append(x)
        
        # Empty minItems
        if not self.minItems:
            self.minItems.append([x, 1])
        elif self.minItems[-1][0] == x:
            self.minItems[-1][1] += 1
        elif x < self.minItems[-1][0]:
            self.minItems.append([x, 1])
        

    def pop(self) -> None:
        top = self.items[-1]
        
        # When item to pop is also on min items
        if top == self.minItems[-1][0]:
            if self.minItems[-1][1] == 1:
                self.minItems.pop()
            else:
                self.minItems[-1][1] -= 1
        
        return self.items.pop()
        

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.minItems[-1][0]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()