class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

# An example for a Deque of numbers
myDq = Deque()
print(myDq.isEmpty())       #check if the deque is empty
myDq.addFront(2)
myDq.addFront(3)
myDq.addRear(1)
myDq.addRear(0)
print(myDq.isEmpty())
print(myDq.size())
myDq.removeRear()
myDq.removeFront()
print(myDq.size())         #check if the elements were removed.