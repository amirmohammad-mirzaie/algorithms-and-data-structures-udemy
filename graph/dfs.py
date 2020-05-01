class Node(object):
    def __init__(self, name):
        self.name = name # name of the node
        self.adj_list = [] # list of nodes that are in the adjacency list
        self.visited = False # visited or not
        self.pred = None # predecessor of the node

class DepthFirstSearch(object):
    def dfs(self, start_node):
        start_node.visited = True
        print('%s' % start_node.name)

        # for items in the adjacency list of the current node
        for n in start_node.adj_list:
            if not n.visited:
                self.dfs(n)


node1 = Node('a')
node2 = Node('b')
node3 = Node('c')
node4 = Node('d')
node5 = Node('e')

node1.adj_list.append(node2)
node1.adj_list.append(node3)
node2.adj_list.append(node4)
node4.adj_list.append(node5)

dfs = DepthFirstSearch()
dfs.dfs(node1)
