class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkesList:
    def __init__(self):
        self.head =None

    def insert_at_beginig(self, data):
        node = Node(data, self.head)
        self.head = node

    def Print(self):
        if self.head is None:
            print("my link list is empty!")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' -->'
            itr = itr.next
        print(llstr)
    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_list_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)

    def count_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index > self.count_length():
            raise Exception("Invalid length")
        elif index == 0:
            self.head = self.head.next
            return
        count = 0

        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at_index(self, data, index):
        if index < 0 or index > self.count_length():
            raise Exception("Invalid length")
        elif index == 0:
            self.insert_at_beginig(data)
            return
        cound = 0
        itr = self.head
        while itr:
            if cound == index -1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            cound = cound + 1


if __name__ == '__main__':
    obj = LinkesList()
    obj.insert_list_value(['mango', 'banana', 'orange'])
    print(obj.count_length())
    obj.insert_at_index('ramboottan', 1)
    obj.insert_at_index('jackfrout', 3)
    obj.Print()