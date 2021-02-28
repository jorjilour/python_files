from queue import Queue
import sys

# Initializing a queue
q = Queue(maxsize=3)

# qsize() give the maxsize 
# of the Queue 
print(q.qsize())

# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')

# Return Boolean for Full 
# Queue 
print("\nFull: ", q.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty 
# Queue 
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())

# QUEUE USING LIST #
# Python program to
# demonstrate queue implementation
# using list

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# QUEUE.DEQUE

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# QUEUE AS A CLASS #


class MyQueue:

    def __init__(self, maxsize=sys.maxsize):
        self.queue = []
        self.maxsize = maxsize

    def __str__(self):
        return str(self.queue)

    def is_empty(self):
        return self.queue == []

    def is_full(self):
        return len(self.queue) == self.maxsize

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def last(self):
        if self.is_empty():
            return None
        return self.queue[-1]

    def size(self):
        return len(self.queue)


myQ = MyQueue(maxsize=9)
myQ.enqueue(1)
myQ.enqueue(2)
myQ.enqueue(3)
myQ.enqueue(4)

print(myQ)

myQ.dequeue()
print(myQ)


myQ.dequeue()
print(myQ)
print(myQ.maxsize)
