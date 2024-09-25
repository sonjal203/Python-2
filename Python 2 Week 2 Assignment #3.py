class Queue:
    def __init__(self):
        self.items = []  # Initialize the queue as an empty list

    def enqueue(self, item):
        self.items.append(item)  # Add item to the end of the list

    def dequeue(self):
        if not self.items:
            raise Exception("Queue is empty")
        return self.items.pop(0)  # Remove and return item from the front of the list

    def isempty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Test cases
q = Queue()
print(q.isempty())  # True

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.size())  # 3

print(q.dequeue())  # 10
print(q.dequeue())  # 20

print(q.isempty())  # False