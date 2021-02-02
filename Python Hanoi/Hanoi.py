# Question: If I have n disks, move disks into designated peg.
# Rule 01: Larger disk cannot be on top of the smaller disk
# Rule 02: Should move the disk on top first

'''
    peg i           peg j           peg k
    A  
    B
    C
    D
    E
'''
MAX_SIZE = 20 #unnecessary

# Attempt 01: Stack
class Node:
    def __init__(self, data):
        self.data=data

class Stack:
    def __init__(self):
        self.stackList=[]
        self.top=0
        self.tempTop=0

    def push(self, data):
        if not self.isFull():
            newNode=Node(data)
            self.stackList.insert(self.tempTop, newNode)
            self.top += 1
            self.temptop += 1
            print('pushed')
        else:
            print('stack overflow')

    def pop(self):
        if not self.isEmpty():
            print(self.stackList[self.tempTop-1].data)
            result = self.stackList[self.tempTop-1]
            self.tempTop -= 1
            return 
        else:
            print('stack empty')
            return -1

    def isEmpty(self):
        return self.tempTop == 0

    def isFull(self):
        return self.top==MAX_SIZE

def directMove(origin, dest):
    push(pop())

def move(n, i, j, k):
    self.move(n-1, i, j, k)
    push()

#Setting up
ii.Stack()
jj.Stack()
kk.Stack()
num=input('Insert how many disks you have')
for i in range(1,input):
    ii.push(char('A'+i))






# Attempt 02: Linear Linked List(LA??)