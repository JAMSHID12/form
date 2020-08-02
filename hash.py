class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [ [] for i in range(self.max)]

    def get_hash(self, key):
        hash = 0
        for item in key:
            hash += ord(item)
        return hash % self.max

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        fount = False
        for idx, elements in enumerate(self.arr[h]):
            if len(elements) == 2 and elements[0]==key:
                self.arr[h][idx] = (key, value)
                fount = True
                break
        if not fount:
            self.arr[h].append((key, value))


t = HashTable()
t['march 6'] = 120
t['march 8'] = 67
t['march 9'] = 4
t['march 17'] = 459
print(t.arr)

