"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # pass  # TODO

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            # self.vertices[v2].add(v1)
        else:
            print('No vertex at here')
            raise KeyError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        q = Queue()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        return visited

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            next_visited = s.pop()
            if next_visited not in visited:
                visited.add(next_visited)
                print(next_visited)
                for next_vertex in self.vertices[next_visited]:
                    s.push(next_vertex)

    def dft_recursive_h(self, v, visited, stack):
        if stack.size() > 0:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for next_vertex in self.vertices[v]:
                    stack.push(next_vertex)
            self.dft_recursive_h(v, visited, stack)
        else:
            return False

    def dft_recursive(self, starting_vertex, visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        self.dft_recursive_h(starting_vertex, visited, s)
        return visited

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        q.enqueue([starting_vertex])
        while q.size() > 0:
            vertex = q.dequeue()
            last_vertex = vertex[-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return vertex
                visited.add(last_vertex)
                for next_vertex in self.vertices[last_vertex]:
                    path = list(vertex)
                    path.append(next_vertex)
                    q.enqueue(path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        # push a list holding the starting vertex id
        s.push([starting_vertex])
        # created an empty visited set
        visited = set()
        # while the stack is not empty
        while s.size() > 0:
            # pop to the path
            vertex = s.pop()
            # set a vert to the last item in the path
            last_vertex = vertex[-1]
            # if vert is not in visited
            if last_vertex not in visited:
                # if vert is equal to target value
                if last_vertex == destination_vertex:
                    # return path
                    return vertex
                # add vert to visited set
                visited.add(last_vertex)
                # loop over next vert in vertices at the index of vert
                for next_vert in self.vertices[last_vertex]:
                    # set a new path equal to a new list of the path (copy)
                    path = list(vertex)
                    # append next vert to new path
                    path.append(next_vert)
                    # push the new path
                    s.push(path)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path is None:
            path = [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors - set(path):
            findPath = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor])
            if findPath is not None:
                return findPath

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
