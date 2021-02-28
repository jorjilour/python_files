import sys


class Stack:
    def __init__(self, maxsize=sys.maxint):
        self.stack = []
        self.maxsize = maxsize

    def __str__(self):
        return str(self.stack)

    def is_empty(self):
        return self.stack == []

    def is_full(self):
        return len(self.stack) == self.maxsize

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack)

stack.pop()
print(stack)

stack.pop()
print(stack)



# STACK AS LIST #

stack = ['a', 'b', 'c']

stack.append('d')

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# STACKS AS COLLECTIONS DEQUE #

from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print("stack: " + str(stack))

stack.pop()
stack.pop()

print('\nStack after elements are popped:')
print(stack)

# STACK AS QUEUE.LIFOQUEUE #

import queues
# Initializing a stack
stack = LifoQueue(maxsize=3)

# qsize() show the number of elements
# in the stack
print(stack.qsize())

# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

# get() fucntion to pop
# element from stack in
# LIFO order
print('\nElements poped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())

