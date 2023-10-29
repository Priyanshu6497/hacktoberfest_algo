class UnionFind:
    
    def __init__(self, sz):
        self.root = [i for i in range(sz)]
    
    def find(self, x):
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
               

class Graph:
    
    def __init__(self, V):
        self.V = V
        self.adj = []
    
    def addEdge(self, x, y, w):
        self.adj.append([x, y, w])
    
    def kruskals(self):
        # self.adj.sort(key = lambda x: x[2])
        ans = []
        cost = 0
        
        uf = UnionFind(self.V)
        for edge in sorted(self.adj, key = lambda x: x[2]):
            if uf.find(edge[0]) != uf.find(edge[1]):
                ans.append([edge[0], edge[1]])
                cost += edge[2]
                uf.union(edge[0], edge[1])
                
        return ans, cost

g = Graph(4)
g.addEdge(0, 1, 1)
g.addEdge(1, 3, 3)
g.addEdge(3, 2, 4)
g.addEdge(2, 0, 2)
g.addEdge(0, 3, 2)
g.addEdge(1, 2, 2)

print(g.kruskals())