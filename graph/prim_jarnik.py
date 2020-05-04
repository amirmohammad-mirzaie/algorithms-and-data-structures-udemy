import heapq

# vertex class used in the graph class
class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
    # setter
    def set_name(self, name):
        self.name = name
    # getter
    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

    # adding new vertex neighbor nodes to the vertex
    def add_neighbor(self, to_vertex, weight):
        self.neighbors[to_vertex] = weight
    # getter
    def get_neighbors(self):
        return self.neighbors
    # getter
    def get_edge_weight(self, neighbor):
        return self.neighbors[neighbor]

# edge class
class Edge(object):
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex
    # method for comparing two Edge objects
    def __lt__(self, other):
        self_weight = self.weight
        other_weight = other.weight
        return self_weight < other_weight

# graph class used to create a graph from input vertices
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    # adding new vertex
    def add_vertex(self, id):
        self.num_vertices += 1
        new_vertex = Vertex(id)
        self.vert_dict[id] = new_vertex
        return new_vertex
    # getter
    def get_vertex(self, id):
        if id in self.vert_dict:
            return self.vert_dict[id]
        else:
            return None

    # adding new edge
    # if you want to make it directed graph,
    # simply comment self.vert_dict[to_id].........
    def add_edge(self, from_id, to_id, weight):
        if from_id not in self.vert_dict:
            self.add_vertex(from_id)
        if to_id not in self.vert_dict:
            self.add_vertex(to_id)

        self.vert_dict[from_id].add_neighbor(self.vert_dict[to_id], weight)
        self.vert_dict[to_id].add_neighbor(self.vert_dict[from_id], weight)

    # getter
    def get_vertices_keys(self):
        return self.vert_dict.keys()

    # used to create unvisited vertices
    def get_vertices_dict_copy(self):
        unvisited_dict = {}
        for id in self.get_vertices_keys():
            unvisited_dict[id] = self.vert_dict[id]
        return unvisited_dict


class PrimsJarnik(object):
    def __init__(self, graph):
        self.graph = graph
        self.spanning_tree = [] # list of selected edges
        self.edge_heap = []
        self.full_cost = 0

    # main algorithm goes here
    def calculate_spanning_tree(self, start_vertex_name):
        # getting a vertex corresponding to it's name
        vertex = self.graph.get_vertex(start_vertex_name)

        # getting the list of all vertices as unvisited list
        unvisited_dict = self.graph.get_vertices_dict_copy()

        # removing this vertex from the dictionary
        del unvisited_dict[vertex.get_name()]
        
        # while we have an unvisited vertex
        while unvisited_dict:
            # for each neighbor vertex in the vertex's neighbors
            for neighbor_vertex in vertex.get_neighbors():
                # if this neighbor is not visited
                if neighbor_vertex.get_name() in unvisited_dict:
                    # get the weight of the edge connecting the two vertices
                    weight = vertex.get_edge_weight(neighbor_vertex)
                    # creating an edge object
                    edge = Edge(weight, vertex, neighbor_vertex)
                    # add it to the heap
                    heapq.heappush(self.edge_heap, edge)

            # getting the edge with lowest value
            min_edge = heapq.heappop(self.edge_heap)
            # if this edge's target_vertex is not visited
            if unvisited_dict[min_edge.target_vertex.get_name()]:
                # append this edge to the spanning tree's list
                self.spanning_tree.append(min_edge)
                print('edge added to the spanning tree: %s-%s' %(min_edge.start_vertex.get_name(),
                                                                 min_edge.target_vertex.get_name()))
                # sum up the edge's weight to the full_cost variable
                self.full_cost += min_edge.weight
                # set the vertex to be the edge's target vertex
                vertex = min_edge.target_vertex
                # remove the current vertex from the unvisited dictionary
                del unvisited_dict[vertex.get_name()]
    # getter
    def get_spanning_tree(self):
        return self.spanning_tree
    # getter
    def get_cost(self):
        return self.full_cost


# creating the graph
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_vertex('G')

graph.add_edge('A', 'B', 2)
graph.add_edge('A', 'E', 5)
graph.add_edge('A', 'C', 6)
graph.add_edge('A', 'F', 10)
graph.add_edge('B', 'E', 3)
graph.add_edge('B', 'D', 3)
graph.add_edge('C', 'D', 1)
graph.add_edge('C', 'F', 2)
graph.add_edge('D', 'E', 4)
graph.add_edge('D', 'G', 5)
graph.add_edge('F', 'G', 3)

# testing the algorithm
algorithm = PrimsJarnik(graph)
algorithm.calculate_spanning_tree('D')
print(algorithm.get_cost())
