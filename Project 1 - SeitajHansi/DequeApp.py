#2c
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

# People entering and leaving a train or a bus
# Using deque for a train functionality
train = Deque()

train.addRear('Bob')
train.addRear('Jordan')
train.addRear('Eni')
train.addRear('Hansi')
train.addFront('George')
train.addFront('Hary')
train.addFront('Mike')
train.addFront('Emily')
print('Is the train empty? {}'.format(train.isEmpty()))
print('How many people are in the train? {}'.format(train.size()))
train.removeRear()
train.removeFront()
print('How many people are in the train now? {}'.format(train.size()))
train.removeFront()
train.removeFront()
train.removeFront()
train.removeRear()
train.removeRear()
train.removeRear()
print('How many people are in the train now? {}'.format(train.size()))
print('Is the train empty? {}'.format(train.isEmpty()))


