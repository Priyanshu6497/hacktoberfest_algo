import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # Assuming an undirected graph

    def min_distance(self, dist, visited):
        min_dist = sys.maxsize
        min_index = -1

        for v in range(self.vertices):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, source):
        dist = [sys.maxsize] * self.vertices
        dist[source] = 0
        visited = [False] * self.vertices

        for _ in range(self.vertices):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v in range(self.vertices):
                if (
                    self.graph[u][v]
                    and visited[v] is False
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_solution(dist)

    def print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.vertices):
            print(node, "\t", dist[node])


# Example usage
if __name__ == "__main__":
    graph = Graph(6)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 4)
    graph.add_edge(3, 4, 2)
    graph.add_edge(4, 5, 6)

    graph.dijkstra(0)
