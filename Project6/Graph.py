"""
Name:
CSE 331 FS20 (Onsay)
"""

import heapq
import itertools
import math
import queue
import time
from typing import TypeVar, Callable, Tuple, List, Set

import matplotlib.cm as cm
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np

T = TypeVar('T')
Matrix = TypeVar('Matrix')  # Adjacency Matrix
Vertex = TypeVar('Vertex')  # Vertex Class Instance
Graph = TypeVar('Graph')  # Graph Class Instance


class Vertex:
    """ Class representing a Vertex object within a Graph """

    __slots__ = ['id', 'adj', 'visited', 'x', 'y']

    def __init__(self, idx: str, x: float = 0, y: float = 0) -> None:
        """
        DO NOT MODIFY
        Initializes a Vertex
        :param idx: A unique string identifier used for hashing the vertex
        :param x: The x coordinate of this vertex (used in a_star)
        :param y: The y coordinate of this vertex (used in a_star)
        """
        self.id = idx
        self.adj = {}  # dictionary {id : weight} of outgoing edges
        self.visited = False  # boolean flag used in search algorithms
        self.x, self.y = x, y  # coordinates for use in metric computations

    def __eq__(self, other: Vertex) -> bool:
        """
        DO NOT MODIFY
        Equality operator for Graph Vertex class
        :param other: vertex to compare
        """
        if self.id != other.id:
            return False
        elif self.visited != other.visited:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex visited flags not equal: self.visited={self.visited},"
                  f" other.visited={other.visited}")
            return False
        elif self.x != other.x:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex x coords not equal: self.x={self.x}, other.x={other.x}")
            return False
        elif self.y != other.y:
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex y coords not equal: self.y={self.y}, other.y={other.y}")
            return False
        elif set(self.adj.items()) != set(other.adj.items()):
            diff = set(self.adj.items()).symmetric_difference(set(other.adj.items()))
            print(f"Vertex '{self.id}' not equal")
            print(f"Vertex adj dictionaries not equal:"
                  f" symmetric diff of adjacency (k,v) pairs = {str(diff)}")
            return False
        return True

    def __repr__(self) -> str:
        """
        DO NOT MODIFY
        Represents Vertex object as string.
        :return: string representing Vertex object
        """
        lst = [f"<id: '{k}', weight: {v}>" for k, v in self.adj.items()]

        return f"<id: '{self.id}'" + ", Adjacencies: " + "".join(lst) + ">"

    def __str__(self) -> str:
        """
        DO NOT MODIFY
        Represents Vertex object as string.
        :return: string representing Vertex object
        """
        return repr(self)

    def __hash__(self) -> int:
        """
        DO NOT MODIFY
        Hashes Vertex into a set; used in unit tests
        :return: hash value of Vertex
        """
        return hash(self.id)

    # ============== Modify Vertex Methods Below ==============#

    def degree(self) -> int:
        """
        returns the degree
        :return:integer degree
        """
        return len(self.adj)

    def get_edges(self) -> Set[Tuple[str, float]]:
        """
        returns the edge list with weight
        :return: tuple with edges and list
        """
        if self.degree() == 0:
            return set()
        final = set()

        for key in self.adj:
            final.add((key, self.adj[key]))

        return final

    def euclidean_distance(self, other: Vertex) -> float:
        """
        Computes th eEuclidian distance
        :param other: Vertex and self
        :return: distance in float
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** (1 / 2)

    def taxicab_distance(self, other: Vertex) -> float:
        """
        Computes the taxicab distance
        :param other: vertex and self vertex
        :return: distance in float
        """
        return abs(self.x - other.x) + abs(self.y - other.y)


class Graph:
    """ Class implementing the Graph ADT using an Adjacency Map structure """

    __slots__ = ['size', 'vertices', 'plot_show', 'plot_delay']

    def __init__(self, plt_show: bool = False, matrix: Matrix = None, csv: str = "") -> None:
        """
        DO NOT MODIFY
        Instantiates a Graph class instance
        :param: plt_show : if true, render plot when plot() is called; else, ignore calls to plot()
        :param: matrix : optional matrix parameter used for fast construction
        :param: csv : optional filepath to a csv containing a matrix
        """
        matrix = matrix if matrix else np.loadtxt(csv, delimiter=',', dtype=str).tolist() if csv else None
        self.size = 0
        self.vertices = {}

        self.plot_show = plt_show
        self.plot_delay = 0.2

        if matrix is not None:
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix)):
                    if matrix[i][j] == "None" or matrix[i][j] == "":
                        matrix[i][j] = None
                    else:
                        matrix[i][j] = float(matrix[i][j])
            self.matrix2graph(matrix)

    def __eq__(self, other: Graph) -> bool:
        """
        DO NOT MODIFY
        Overloads equality operator for Graph class
        :param other: graph to compare
        """
        if self.size != other.size or len(self.vertices) != len(other.vertices):
            print(f"Graph size not equal: self.size={self.size}, other.size={other.size}")
            return False
        else:
            for vertex_id, vertex in self.vertices.items():
                other_vertex = other.get_vertex(vertex_id)
                if other_vertex is None:
                    print(f"Vertices not equal: '{vertex_id}' not in other graph")
                    return False

                adj_set = set(vertex.adj.items())
                other_adj_set = set(other_vertex.adj.items())

                if not adj_set == other_adj_set:
                    print(f"Vertices not equal: adjacencies of '{vertex_id}' not equal")
                    print(f"Adjacency symmetric difference = "
                          f"{str(adj_set.symmetric_difference(other_adj_set))}")
                    return False
        return True

    def __repr__(self) -> str:
        """
        DO NOT MODIFY
        Represents Graph object as string.
        :return: String representation of graph for debugging
        """
        return "Size: " + str(self.size) + ", Vertices: " + str(list(self.vertices.items()))

    def __str__(self) -> str:
        """
        DO NOT MODIFY
        Represents Graph object as string.
        :return: String representation of graph for debugging
        """
        return repr(self)

    def plot(self) -> None:
        """
        DO NOT MODIFY
        Creates a plot a visual representation of the graph using matplotlib
        :return: None
        """
        if self.plot_show:

            # if no x, y coords are specified, place vertices on the unit circle
            for i, vertex in enumerate(self.get_vertices()):
                if vertex.x == 0 and vertex.y == 0:
                    vertex.x = math.cos(i * 2 * math.pi / self.size)
                    vertex.y = math.sin(i * 2 * math.pi / self.size)

            # show edges
            num_edges = len(self.get_edges())
            max_weight = max([edge[2] for edge in self.get_edges()]) if num_edges > 0 else 0
            colormap = cm.get_cmap('cool')
            for i, edge in enumerate(self.get_edges()):
                origin = self.get_vertex(edge[0])
                destination = self.get_vertex(edge[1])
                weight = edge[2]

                # plot edge
                arrow = patches.FancyArrowPatch((origin.x, origin.y),
                                                (destination.x, destination.y),
                                                connectionstyle="arc3,rad=.2",
                                                color=colormap(weight / max_weight),
                                                zorder=0,
                                                **dict(arrowstyle="Simple,tail_width=0.5,"
                                                                  "head_width=8,head_length=8"))
                plt.gca().add_patch(arrow)

                # label edge
                plt.text(x=(origin.x + destination.x) / 2 - (origin.x - destination.x) / 10,
                         y=(origin.y + destination.y) / 2 - (origin.y - destination.y) / 10,
                         s=weight, color=colormap(weight / max_weight))

            # show vertices
            x = np.array([vertex.x for vertex in self.get_vertices()])
            y = np.array([vertex.y for vertex in self.get_vertices()])
            labels = np.array([vertex.id for vertex in self.get_vertices()])
            colors = np.array(
                ['yellow' if vertex.visited else 'black' for vertex in self.get_vertices()])
            plt.scatter(x, y, s=40, c=colors, zorder=1)

            # plot labels
            for j, _ in enumerate(x):
                plt.text(x[j] - 0.03 * max(x), y[j] - 0.03 * max(y), labels[j])

            # show plot
            plt.show()
            # delay execution to enable animation
            time.sleep(self.plot_delay)

    # ============== Modify Graph Methods Below ==============#

    def reset_vertices(self) -> None:
        """
        Resets vertex param visited as false
        :return:None
        """
        for key in self.vertices:
            self.vertices[key].visited = False

    def get_vertex(self, vertex_id: str) -> Vertex:
        """
        return the vertex with the id
        :param vertex_id: find the vertex with this id
        :return: Vertex found from id
        """
        try:
            return self.vertices[vertex_id]
        except:
            return None

    def get_vertices(self) -> Set[Vertex]:
        """
        return vertices in the graph
        :return: set of vertices
        """
        if len(self.vertices) == 0:
            return set()
        final = set()
        for key in self.vertices:
            final.add(self.vertices[key])
        return final

    def get_edge(self, start_id: str, dest_id: str) -> Tuple[str, str, float]:
        """
        Returns the edge
        :param start_id: start id
        :param dest_id:  end id
        :return: tuple of edge found between the two vertwx
        """
        if self.get_vertex(start_id) is None or self.get_vertex(dest_id) is None:
            return None
        try:
            if self.get_vertex(start_id).adj[dest_id] is None:
                return None
        except:
            return None
        return start_id, dest_id, self.get_vertex(start_id).adj[dest_id]

    def get_edges(self) -> Set[Tuple[str, str, float]]:
        """
        Returns the edges of the graph
        :return: set of edges with vertex and weight information
        """
        final = set()

        for key in self.vertices:
            for key1 in self.vertices[key].adj:
                final.add(self.get_edge(key, key1))
        return final

    def add_to_graph(self, start_id: str, dest_id: str = None, weight: float = 0) -> None:
        """
        add the vertex or an edge to a graph
        :param start_id: start vertex to add (if required)
        :param dest_id: end vertex id required to add (if required)
        :param weight: weight of vertex to add
        :return: None
        """
        if self.get_vertex(start_id) is None:
            self.vertices[start_id] = Vertex(start_id)
            self.size += 1
        if dest_id is not None:
            if self.get_vertex(dest_id) is None:
                self.vertices[dest_id] = Vertex(dest_id)
                self.size += 1

            self.get_vertex(start_id).adj[dest_id] = weight

    def matrix2graph(self, matrix: Matrix) -> None:
        """
        Converts a matrix to a graph
        :param matrix: matrix to convert
        :return: NOne
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i != 0 and j != 0:
                    self.add_to_graph(matrix[i][0], None, 0)
                    self.add_to_graph(matrix[0][j], None, 0)

                if matrix[i][j] is not None and i != 0 and j != 0:
                    self.add_to_graph(matrix[i][0], matrix[0][j], matrix[i][j])

    def graph2matrix(self) -> Matrix:
        """
        converts the current graph to matrix
        :return: the matrix obtained with conversion
        """
        if self.size == 0:
            return None
        rows, cols = (self.size + 1, self.size + 1)
        matrix = [[None for i in range(cols)] for j in range(rows)]

        count = 1
        for i in self.vertices:
            matrix[0][count] = i
            matrix[count][0] = i
            count += 1

        for i in range(self.size + 1):
            for j in range(self.size + 1):
                if i != 0 and j != 0:
                    vertex = self.get_vertex(matrix[i][0])
                    if vertex is not None:
                        if matrix[0][j] in vertex.adj:
                            matrix[i][j] = vertex.adj[matrix[0][j]]

        return matrix

    def bfs(self, start_id: str, target_id: str) -> Tuple[List[str], float]:
        """
        breadth first traversal on a graph
        :param start_id:id of vertex to start with
        :param target_id: id of vertex of when to stop
        :return: returns the path and the weight required to traverse
        """
        path = {}
        final = []

        if self.get_vertex(start_id) is not None and self.get_vertex(target_id) is not None:
            distance = {self.vertices[start_id]: 0}

            vertex = self.get_vertex(start_id)
            vertex.visited = True
            Qu = queue.SimpleQueue()
            Qu.put(vertex)

            while not Qu.empty():
                vertex_popped = Qu.get()
                for i in vertex_popped.adj:
                    if not self.vertices[i].visited:
                        path[self.vertices[i]] = vertex_popped
                        distance[self.vertices[i]] = vertex_popped.adj[i] + distance[vertex_popped]

                        self.vertices[i].visited = True
                        Qu.put(self.get_vertex(i))

            if len(path) == 0:
                return [], 0
            if self.vertices[target_id] not in path:
                return [], 0

            final.append(target_id)
            vertex = self.vertices[target_id]
            while vertex is not self.vertices[start_id]:
                vertex = path[vertex]
                final.append(vertex.id)
            final.reverse()

            return final, distance[self.vertices[target_id]]

        return [], 0

    def dfs(self, start_id: str, target_id: str) -> Tuple[List[str], float]:
        """
        depth first traversal for the graph (helper)
        :param start_id:id of vertex to start with
        :param target_id: id of vertex of when to stop
        :return: returns the path and the weight required to traverse
        """
        path = []

        def dfs_inner(current_id: str, target_id: str, path: List[str] = []) \
                -> Tuple[List[str], float]:
            """
            depth first traversal for the graph
            :param current_id: id of vertex to start with
            :param target_id: id of vertex of when to stop
            :param path: list to add the path traversals to
            :return: tuple of path traversed with weight
            """
            if current_id not in path:

                path.append(current_id)
                if target_id in self.vertices[current_id].adj:
                    path.append(target_id)
                    return path, self.get_edge(current_id, target_id)[2]

                for i in self.get_vertex(current_id).adj:
                    self.vertices[current_id].visited = True
                    if i != target_id:
                        if not self.vertices[i].visited:
                            distance = self.get_edge(current_id, i)[2]
                            path, distance = dfs_inner(i, target_id, path)

                            # path.append(i)
                            distance += self.get_vertex(current_id).adj[i]
                            return path, distance
                    else:
                        path.append(i)
                        return path, self.get_edge(current_id, i)[2]
            return [], 0

        if self.size == 0:
            return [], 0
        if self.get_vertex(start_id) is not None and self.get_vertex(target_id) is not None:

            path, distance = dfs_inner(start_id, target_id, path)
            if len(path) == 1 or len(path) == 0:
                return [], 0
            return path, distance
        else:
            return path, 0

        return path, 0

    def a_star(self, start_id: str, target_id: str, metric: Callable[[Vertex, Vertex], float]) \
            -> Tuple[List[str], float]:
        """
        This function founds the shortest path between two vertices using A* search
        :param start_id: start vertex id
        :param target_id: target vertex id
        :param metric: to compute the distance through heuristic function
        :return:
        """
        d = {}  # d[v] is upper bound from s to v
        cloud = {}  # map reachable v to its d[v] value
        pq = AStarPriorityQueue()  # vertex v will have key d[v]
        path = {}
        # for each vertex v of the graph, add an entry to the priority queue, with
        # the source having distance 0 and all others having infinite distance
        for id in self.vertices:
            if id == start_id:
                d[self.vertices[id]] = 0
                self.vertices[id].visited = True
            else:
                d[self.vertices[id]] = float('inf')  # syntax for positive infinity
            pq.push(d[self.vertices[id]], self.vertices[id])  # save locator for future updates

        while not pq.empty():
            key, u = pq.pop()
            cloud[u] = key  # its correct d[u] value
            if u.id == target_id:
                break
            for e in u.adj:  # outgoing edges (u,v)
                v = self.vertices[e]
                if v not in cloud and not v.visited:
                    candidate_distance = self.get_edge(u.id, v.id)[2]
                    # perform relaxation step on edge (u,v)
                    wgt = self.get_edge(u.id, v.id)[2]
                    if wgt + d[u] < d[v]:  # is this a new shorter path to v through u?
                        d[v] = d[u] + wgt  # update the TRUE distance to v through u
                        pq.update(d[v] + metric(self.vertices[target_id], v), v)
                        path[self.vertices[e]] = u

        final = []
        final.append(target_id)
        vertex = self.vertices[target_id]
        while vertex is not self.vertices[start_id]:
            vertex = path[vertex]
            final.append(vertex.id)
        final.reverse()

        distance = 0
        lent = len(final)
        for i in range(len(final)):
            if i + 1 < lent:
                distance += self.get_edge(final[i], final[i + 1])[2]

        return final, distance

    def make_equivalence_relation(self) -> int:
        """
        Description.
        :return:
        """
        pass


class AStarPriorityQueue:
    """
    Priority Queue built upon heapq module with support for priority key updates
    Created by Andrew McDonald
    Inspired by https://docs.python.org/3/library/heapq.html
    """

    __slots__ = ['data', 'locator', 'counter']

    def __init__(self) -> None:
        """
        Construct an AStarPriorityQueue object
        """
        self.data = []  # underlying data list of priority queue
        self.locator = {}  # dictionary to locate vertices within priority queue
        self.counter = itertools.count()  # used to break ties in prioritization

    def __repr__(self) -> str:
        """
        Represent AStarPriorityQueue as a string
        :return: string representation of AStarPriorityQueue object
        """
        lst = [f"[{priority}, {vertex}], " if vertex is not None else "" for
               priority, count, vertex in self.data]
        return "".join(lst)[:-1]

    def __str__(self) -> str:
        """
        Represent AStarPriorityQueue as a string
        :return: string representation of AStarPriorityQueue object
        """
        return repr(self)

    def empty(self) -> bool:
        """
        Determine whether priority queue is empty
        :return: True if queue is empty, else false
        """
        return len(self.data) == 0

    def push(self, priority: float, vertex: Vertex) -> None:
        """
        Push a vertex onto the priority queue with a given priority
        :param priority: priority key upon which to order vertex
        :param vertex: Vertex object to be stored in the priority queue
        :return: None
        """
        # list is stored by reference, so updating will update all refs
        node = [priority, next(self.counter), vertex]
        self.locator[vertex.id] = node
        heapq.heappush(self.data, node)

    def pop(self) -> Tuple[float, Vertex]:
        """
        Remove and return the (priority, vertex) tuple with lowest priority key
        :return: (priority, vertex) tuple where priority is key,
        and vertex is Vertex object stored in priority queue
        """
        vertex = None
        while vertex is None:
            # keep popping until we have valid entry
            priority, count, vertex = heapq.heappop(self.data)
        del self.locator[vertex.id]  # remove from locator dict
        vertex.visited = True  # indicate that this vertex was visited
        while len(self.data) > 0 and self.data[0][2] is None:
            heapq.heappop(self.data)  # delete trailing Nones
        return priority, vertex

    def update(self, new_priority: float, vertex: Vertex) -> None:
        """
        Update given Vertex object in the priority queue to have new priority
        :param new_priority: new priority on which to order vertex
        :param vertex: Vertex object for which priority is to be updated
        :return: None
        """
        node = self.locator.pop(vertex.id)  # delete from dictionary
        node[-1] = None  # invalidate old node
        self.push(new_priority, vertex)  # push new node
