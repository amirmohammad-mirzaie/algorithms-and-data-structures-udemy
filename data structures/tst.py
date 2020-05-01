class Node(object):
    def __init__(self, char):
        self.char = char
        self.left_node = None
        self.middle_node = None
        self.right_node = None
        self.value = -1


class TST(object):

    def __init__(self):
        self.root_node = None
    # putting items into the TST
    def put(self, key, value):
        self.root_node = self.put_item(self.root_node, key, value, 0)

    # helper method for putting items
    def put_item(self, node, key, value, index):
        c = key[index]
        # if there is no node currrently, we just create one
        if node is None:
            node = Node(c)

        # otherwise, we know that there is a node

        # if the current character (c) is less than the node's current character
        # we go to the left child of the node
        if c < node.char:
            node.left_node = self.put_item(node.left_node, key, value, index)

        # if the current character (c) is greater than the node's current character
        # we go to the left child of the node
        elif c > node.char:
            node.right_node = self.put_item(node.right_node, key, value, index)

        # certainly the current character is equal to the current node's character
        # so we check if it is the latest character or not
        elif index < len(key)-1:
            index += 1
            node.middle_node = self.put_item(node.middle_node, key, value, index)

        # for certain, it is the latest character
        # so we add the value here
        else:
            node.value = value

        return node

    # getting an item by it's key.
    # returns -1 if it doesn't exist
    def get(self, key):
        node = self.get_item(self.root_node, key, 0)
        if not node:
            return -1
        return node.value

    # helper method for getting an item
    def get_item(self, node, key, index):
        if not node:
            return None

        if key[index] < node.char:
            return self.get_item(node.left_node, key, index)
        elif key[index] > node.char:
            return self.get_item(node.right_node, key, index)
        elif index < len(key) -1:
            return self.get_item(node.middle_node, key, index+1)
        else:
            return node


tst = TST()
tst.put('book', 10)
tst.put('programming', 23)
tst.put('brother', 4)
tst.put('booda', 5)
tst.put('prototype', 21)

print(tst.get('prototype'))
print(tst.get('boodah'))
print(tst.get('boo'))
