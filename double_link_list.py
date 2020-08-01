class Node:
    def __init__(self, prev=None,data=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
class Double_linked_list:
    def __init__(self):
        self.head = None

    def inser_beggining(self, data):
        node = Node(None, data, self.head)
        self.head.prev = node
        self.head = node

    def print_list_forword(self):
        if self.head is None:
            print('linklist is empty')
            return
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next
        print(llist)

    def print_backword(self):
        if self.head is None:
            print('list is empty')
            return
        last_node = self.last_node()
        itr = last_node
        llstr = ' '
        while itr:
            llstr += '<--' + str(itr.data)
            itr = itr.prev
        print(llstr)

    def last_node(self):
        itr = self.head
        while itr:
            itr = itr.next
        return itr
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(itr, data, None)

    def insert_values(self, data_list):
        self.head = None
        for item in data_list:
            self.insert_at_end(item)

if __name__ == '__main__':
    dl = Double_linked_list()
    dl.insert_values(['ram', 'dul'])
    dl.print_list_forword()
