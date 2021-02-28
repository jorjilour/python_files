#list as stack
stack = [3,4,5]
stack.append(6)
stack.append(7)

print(stack)

stack.pop()
print(stack)


#list as queues


print("QUEUES")
from collections import deque
names = ["John", "Bob", "Mosh", "Sam", "Mary"]

queue = deque(names)
print(queue)

queue.append("Terry")
queue.append("Graham")
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)







print(names[0])
print(names[-1])
print(names[1:3])
names[0] = "Jon"

print(names)

numbers = [1,2,3,4,5]
print(numbers)

numbers.append(6)
print(numbers)

numbers.insert(0, 0)
print(numbers)

numbers.remove(0)
print(numbers)

#numbers.clear()
#print(numbers)

print(10 in numbers)
print(2 in numbers)

print(len(numbers))

numbers = [2, 2, 3, 4, 5, 6, 6, 4, 3, 3, 3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(numbers)
print(uniques)

