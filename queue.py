class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.remove(self.items[0])

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

q = Queue()
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.dequeue()
q.dequeue()
print(q.display())
print(q.size())
print(q.peek())
