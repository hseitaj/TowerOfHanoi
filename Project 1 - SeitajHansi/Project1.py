#2b
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

#A line at a car wash
def carWash(qu):
    print()
    print("Welcome to carWash! Please enter the line!")
    while not (qu.isEmpty()):
        print("""
                                                              
        {}  ==>   Car Wash  ==>  Clean Car
        __________________________________
        """.format(qu.dequeue()))
        print("Next:")

line = Queue()

line.enqueue('car1')
line.enqueue('car2')
line.enqueue('hyndai2010')
line.enqueue('kia2020')
line.enqueue('Hummer2018')
carWash(line)


