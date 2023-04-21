class Queue:
    def __init__(self):
        self.que = []

    def enqueue(self, item):
        self.que.append(item)

    def dequeue(self):
        return self.que.pop(0)

    def isEmpty(self):
        return self.que == []

    def size(self):
        return len(self.que)

myQ = Queue()
myQ.enqueue(2)
myQ.enqueue(3)
myQ.enqueue(4)
myQ.dequeue()
print(myQ.isEmpty())
print(myQ.size())
