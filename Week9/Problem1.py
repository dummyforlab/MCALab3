class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    vertices = list(graph['vertices'])
    edges = sorted(graph['edges'], key=lambda x: x[2])
    ds = DisjointSet(vertices)

    mst = []
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
    return mst

import heapq
from collections import defaultdict

def prim(graph, start):
    adj = defaultdict(list)
    for u, v, w in graph['edges']:
        adj[u].append((w, v))
        adj[v].append((w, u))

    visited = set()
    min_heap = [(0, start)]
    mst = []
    
    while min_heap and len(visited) < len(graph['vertices']):
        weight, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            for w, v in adj[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v))
            if weight != 0:
                mst.append((u, weight))
    return mst

