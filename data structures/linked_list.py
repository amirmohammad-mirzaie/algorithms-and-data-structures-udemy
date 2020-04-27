# class for node objects
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    # inserting values to the start of the linked list
    def insert_start(self, data):
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node

        else:
            new_node.next_node = self.head
            self.head = new_node

    # removing a data
    def remove_node(self, data):
        if self.head is None:
            return

        self.size -= 1

        current_node = self.head
        previous_node = None

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

    # getting the size of the linked list
    def get_size(self):
        return self.size

    # inserting at the end of the linked list
    # takes O(N) time
    def insert_end(self, data):
        self.size += 1
        new_node = Node(data)

        actual_node = self.head
        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    def traverse_list(self):
        actual_node = self.head
        while actual_node is not None:
            print('%d' % actual_node.data)
            actual_node = actual_node.next_node



ll = LinkedList()
ll.insert_start(10)
ll.insert_start(4)
ll.insert_start(102)
ll.insert_start(7)
ll.insert_start(5)
ll.insert_end(33)
ll.remove_node(102)
