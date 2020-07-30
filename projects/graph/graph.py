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
        pass  # TODO
        self.vertices[vertex_id] = set()
     
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        pass  # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('that vertex is non-existent')


    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        pass  # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        pass  # TODO
    # create queue and add starting vertex

        to_visit = Queue()
        to_visit.enqueue(starting_vertex)
        # create set for visiting vertecies
        visted_ver = set()
        # while to_visit is not empty
        while to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = to_visit.dequeue()
            # if it has not been visited
            if current_vertex not in visted_ver:
                # print
                print(current_vertex)
                # mark as visited, by adding to visited_ver set.
                visted_ver.add(current_vertex)
                # add all unvisted neighbours to queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visted_ver:
                        to_visit.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        pass  # TODO
     # create to_visit stack and add starting vertex
        to_visit = Stack()
        to_visit.push(starting_vertex)
        # create set for visting verticies
        visited_ver = set()
        # while to_visit is not empty
        while to_visit.size() > 0:
            # pop the first vertex on to_visit
            current_vertex = to_visit.pop()
            # if it has not been visited
            if current_vertex not in visited_ver:
                # print vertex
                print(current_vertex)
                # mark as visited by addign to visited_ver
                visited_ver.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_ver:
                        to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()): # create a srt to store visited vertices 
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO
        # check if the node is visited
        # if not
        if (starting_vertex not in visited):
            # mark it as visited
            visited.add(starting_vertex)
            # print
            print(starting_vertex)
            # call dft_recursive on each child
            for neighbpr in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbpr, visited)
    
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO
         # create an empty queue
        q = Queue()
        # enqueue path to the starting vertex
        q.enqueue([starting_vertex])
        # create a set to track vertices we have visited
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # dequeue the first path
            current_path = q.dequeue()
            # get last vertex from the path
            last_vertex = current_path[-1]
            # if vertex has not been visited:
            if last_vertex not in visited:
                # check the destination
                if last_vertex == destination_vertex:
                    return current_path
                # mark is as visited
                visited.add(last_vertex)
                # add a path to its neighbors to the back of the queue
                for v in self.vertices[last_vertex]:
                    # clone path
                    new_path = [*current_path]
                # add neighbor to the back of the queue
                    new_path.append(v)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO
        # create an empty stack
        stack = Stack()
        # push the starting_vertex id onto the stack
        stack.push([starting_vertex])
        # create a set to store visited vertices
        visited = set()
        # while the stack is not empty
        while stack.size() > 0:
            # dequeue the first path
            current_path = stack.pop()
            # get the last vertex from the path
            last_vertex = current_path[-1]
            # it has not been visited:
            if last_vertex not in visited:
                # check destination
                if last_vertex == destination_vertex:
                    return current_path
                # mark it as visited
                visited.add(last_vertex)
                # add path to its neighbors to the back of the queue
                for v in self.vertices[last_vertex]:

                    # clone path
                    new_path = [*current_path]

                # add neighbor to the back of the queue
                    new_path.append(v)
                    stack.push(new_path)
        print("==END DFS==")

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO
        
        if visited == None:
            visited = set()
    
        if path == None:
            path = []

        # add starting vertex to the visited set
        visited.add(starting_vertex)

        # concatonate the starting vert path to the current path
        path = path + [starting_vertex]

        # check if the starting vertex is equal to the target value
        if starting_vertex == destination_vertex:
            return path

        for child_vertex in self.get_neighbors(starting_vertex):
            if child_vertex not in visited:
                new_path = self.dfs_recursive(child_vertex, destination_vertex, visited, path)
                if new_path:
                    return new_path


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
