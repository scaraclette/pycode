class Stack:
    def __init__(self):
        self.items = []
        
    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items)-1]

