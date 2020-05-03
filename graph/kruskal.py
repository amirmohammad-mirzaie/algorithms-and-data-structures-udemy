# vertex in the graph
class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.node = None

# node in the disjoint set
class Node(object):
    def __init__(self, height, node_id, parent_node):
        self.height = height
        self.node_id = node_id
        self.parent_node = parent_node

class Edge(object):
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    # method used when sorting edges
    def __lt__(self, other_node):
        self_weight = self.weight
        other_weight = other_node.weight
        return self_weight < other_weight

class DisjointSet(object):
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list

        # nodes that are in the disjoint set
        self.root_nodes = []

        # a counter for the number of nodes in the disjoint set
        self.node_count = 0

        # every set is composed of 'Node' objects
        self.set_count = 0

        self.make_sets(vertex_list)

    # finding the root node of a node in the disjoint set plus
    # setting parent node of this node and all of it's ancestors to
    # be equal to the root node
    def find(self, node):
        # using the find_helper method for doing the main
        # job (finding the root and setting parent node)
        node = self.find_helper(node)

        # if we have parent node, then return it's node_id
        if node.parent_node:
            return node.parent_node.node_id
        # else return the node's node_id
        else:
            return node.node_id

    # helper method used to do 2 operations,
    # 1st: finding the root node recursively
    # 2nd: setting all of the ancestors of the node to
    # be the root node
    def find_helper(self, node):
        # if the current node does not have any parent,
        # current node is the parent node
        if not node.parent_node:
            return node
        # otherwise, we use the find_helper recursively to find
        # the root node
        node.parent_node = self.find_helper(node.parent_node)

        # return the parent node of the node
        return node.parent_node

    # merges two trees together
    def merge(self, node1, node2):

        # finding the root id of each node
        root_id1 = self.find(node1)
        root_id2 = self.find(node2)

        if root_id1 == root_id2:
            return # they are in the same disjoint_set

        # finding the root nodes of each tree based on their id
        root1 = self.root_nodes[root_id1]
        root2 = self.root_nodes[root_id2]

        # check if first tree is smaller than the second tree
        if root1.height < root2.height:
            # if it is, then we set it's parent_node to be the second tree's root_node
            root1.parent_node = root2

        # else if first tree is bigger than the second tree
        elif root1.height > root2.height:
            # we set the second's parent_node to be the first tree's root_node
            root2.parent_node = root1
        # otherwise we set the second's parent_node to be the first tree's root_node
        else:
            root2.parent_node = root1
            # increment the first tree's root node
            root1.height += 1

    # make the initial set containing of nodes related to each vertex
    def make_sets(self, vertex_list):
        for v in vertex_list:
            self.make_set(v)

    def make_set(self, vertex):
        # create a node corresponding to a vertex
        node = Node(height=0, node_id=len(self.root_nodes), parent_node=None)
        # set the vertex's node to be this created node
        vertex.node = node
        self.root_nodes.append(node)
        self.set_count += 1
        self.node_count += 1


class Kruskal(object):
    def __init__(self):
        # edges that are selected (based on the smallest to biggest value)
        self.selected_edges = []

    # the main algorithm goes here
    def spanning_tree(self, vertex_list, edge_list):
        # create disjoint_set using the vertex_list
        disjoint_set = DisjointSet(vertex_list)

        # sorting the edges based on their weight
        edge_list.sort()
        for edge in edge_list:
            # getting the edge's start_vertex and end_vertex
            u = edge.start_vertex
            v = edge.target_vertex

            # if the root nodes are not the same
            if disjoint_set.find(u.node) != disjoint_set.find(v.node):

                # append this edge, because it does not make any cycle
                self.selected_edges.append(edge)
                # merge the corresponding trees together
                disjoint_set.merge(u.node, v.node)

    # showing edges
    def show_selected_edges(self):
        for edge in self.selected_edges:
            print(edge.start_vertex.name, '_____', edge.target_vertex.name)



# creating vertices
vertex1 = Vertex("a")
vertex2 = Vertex("b")
vertex3 = Vertex("c")
vertex4 = Vertex("d")
vertex5 = Vertex("e")
vertex6 = Vertex("f")
vertex7 = Vertex("g")

# creating edges
edge1 = Edge(2, vertex1, vertex2)
edge2 = Edge(6, vertex1, vertex3)
edge3 = Edge(5, vertex1, vertex5)
edge4 = Edge(10, vertex1, vertex6)
edge5 = Edge(3, vertex2, vertex4)
edge6 = Edge(3, vertex2, vertex5)
edge7 = Edge(1, vertex3, vertex4)
edge8 = Edge(2, vertex3, vertex6)
edge9 = Edge(4, vertex4, vertex5)
edge10 = Edge(5, vertex4, vertex7)
edge11 = Edge(5, vertex6, vertex7)

# appending vertices to the vertex_list
vertex_list = []
vertex_list.append(vertex1)
vertex_list.append(vertex2)
vertex_list.append(vertex3)
vertex_list.append(vertex4)
vertex_list.append(vertex5)
vertex_list.append(vertex6)
vertex_list.append(vertex7)

# appending edges to the edge_list
edge_list = []
edge_list.append(edge1)
edge_list.append(edge2)
edge_list.append(edge3)
edge_list.append(edge4)
edge_list.append(edge5)
edge_list.append(edge6)
edge_list.append(edge7)
edge_list.append(edge8)
edge_list.append(edge9)
edge_list.append(edge10)
edge_list.append(edge11)

# using the algorithm
algorithm = Kruskal()
algorithm.spanning_tree(vertex_list, edge_list)
algorithm.show_selected_edges()
