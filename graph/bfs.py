class Node(object):
    def __init__(self, name):
        self.name = name # name of the node
        self.adj_list = [] # list of nodes that are in the adjacency list
        self.visited = False # visited or not
        self.pred = None # predecessor of the node

class BreadthFirstSearch(object):
    def bfs(self, start_node):
        queue = []
        queue.append(start_node)
        start_node.visited = True

        # while there is an item in the que
        while queue:
            actual_node = queue.pop(0)
            print('%s ' % actual_node.name)

            # for items in the adjacency list of the current node
            for n in actual_node.adj_list:
                # if the node is not visited
                if not n.visited:
                    # set it to visited
                    n.visited = True
                    # add it to the queue
                    queue.append(n)



node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')

node1.adj_list.append(node2)
node1.adj_list.append(node3)
node2.adj_list.append(node4)
node4.adj_list.append(node5)

bfs = BreadthFirstSearch()
bfs.bfs(node1)
