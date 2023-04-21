# Hansi Seitaj
# CMPSC 462
# Tower of Hanoi
# 2a
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

    def get(self, item):  # Get method added for the Tower of Honoi project
        if (item >= 0) and (item < len(self.items)):
            return self.items[item]
        else:
            return 0


def createDisk(stackIn, size):
    if (size < 4) and (size > 0):  # size of the rod have to be 1, 2 or 3
        stackIn.push(size)
    else:
        return "The size must be between 1-3. Please try again"


# The method accepts three stack objects and displays to the user the disks and the rods content.
def showStimulation(stA, stB, stC):
    a = '*' * int(stA.get(2))
    b = '*' * int(stA.get(1))
    c = '*' * int(stA.get(0))

    d = '*' * int(stB.get(2))
    e = '*' * int(stB.get(1))
    f = '*' * int(stB.get(0))

    n = '*' * int(stC.get(2))
    m = '*' * int(stC.get(1))
    g = '*' * int(stC.get(0))

    print("""

        {x}        {x1}        {x2}
        {y}        {y1}        {y2}                        
        {z}        {z1}        {z2}  
        _____________________________        
          """.format(x=a, y=b, z=c, x1=d, y1=e, z1=f, x2=n, y2=m, z2=g))
    print("The contect on rodA: {w}, rodB: {w1}, rodC: {w2}".format(w=[a, b, c], w1=[d, e, f], w2=[n, m, g]))
    print()


rod1 = Stack()
rod2 = Stack()
rod3 = Stack()

print()
# rod1 has three disk with three sizes, starting state
print("Welcome to the mini-game Tower of Honoi!")
createDisk(rod1, 3)  # 3 represent the large disk
createDisk(rod1, 2)  # 2 represent the medium disk
createDisk(rod1, 1)  # 1 represent the small disk
showStimulation(rod1, rod2, rod3)

print("Step 1:")
rod3.push(rod1.pop())  # 1 - the small disk moves on rod3
showStimulation(rod1, rod2, rod3)

print("Step 2:")
rod2.push(rod1.pop())  # 2 - the medium disk moves on rod2
showStimulation(rod1, rod2, rod3)

print("Step 3:")
rod2.push(rod3.pop())  # 1 - the small disk that is on rod3 moves on rod2
print("Note: The medium disk is on rod 2.")
showStimulation(rod1, rod2, rod3)

print("Step 4:")
rod3.push(rod1.pop())  # 3 - the large disk moves on rod3
showStimulation(rod1, rod2, rod3)

print("Step 5:")
rod1.push(rod2.pop())  # 1 - the small disk that is on rod2 moves on rod1
showStimulation(rod1, rod2, rod3)

print("Step 6:")
rod3.push(rod2.pop())  # 2 - the medium disk moves on rod3
showStimulation(rod1, rod2, rod3)

print("Step 7 - Final step:")
rod3.push(rod1.pop())  # 1 - the small disk that was on rod1 moves to rod3
showStimulation(rod1, rod2, rod3)








