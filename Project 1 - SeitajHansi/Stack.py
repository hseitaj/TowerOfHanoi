class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return 0

    def size(self):
        return len(self.items)


myS = Stack()
myS.push(1)
myS.push(2)
myS.push(3)
myS.push(4)
myS.pop()
print(myS.isEmpty())
print(myS.size())
print(myS.peek())
