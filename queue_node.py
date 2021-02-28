import sys


class QNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:

    def __init__(self, maxsize=sys.maxsize):
        self.head = QNode("head")
        self.size = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return len(self.queue) == self.maxsize

    def enqueue(self, value):
        node = QNode(value)
        node.next = None

        if self.is_empty():
            self.head.next = node
            self.size += 1
        else:
            last_node = self.last()
            last_node.next = node
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack")
        remove_node = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove_node.value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.next.value

    def last(self):
        if self.is_empty():
            return None
        else:
            cur = self.head.next
            last_node = cur

            while cur:
                last_node = cur
                cur = cur.next
        return last_node



    def size(self):
        return len(self.queue)


# Driver Code
if __name__ == "__main__":
    my_queue = MyQueue()
    for i in range(1, 11):
        my_queue.enqueue(i)
    print(f"Stack: {my_queue}")

    for _ in range(1, 6):
        removed_node = my_queue.dequeue()
        print(f"Pop: {removed_node}")
    print(f"Stack: {my_queue}")
