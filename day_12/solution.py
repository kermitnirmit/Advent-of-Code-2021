from collections import defaultdict

f = [x for x in open("input.txt").read().strip().split("\n")]

class Graph:

    def __init__(self):
        self.adj = defaultdict(list)

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def explore(self, n, visited, twice=False):
        if n == "end":
            return 1
        c = 0
        for node in self.adj[n]:
            if node.islower():
                if node not in visited:
                    c += self.explore(node, visited.union({node}), twice)
                elif not twice and node not in "startend":
                    # found something that happened twice already so don't go again
                    c += self.explore(node, visited.union({node}), True)
            else:
                c += self.explore(node, visited, twice)
        return c


g = Graph()
for line in f:
    l, r = line.split("-")
    g.addEdge(l,r)

print(g.explore("start", {"start"}, True))
print(g.explore("start", {"start"}, False))
