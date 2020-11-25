class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


s = stack()
s.push(2)
s.push(4)
s.push(6)
s.push(8)
s.push(3)
print(s.peek())
print(s.size())
print(s.is_empty())
print(s.pop())
print(s.display())
