"""Breadth first search algorithm uses queue to get next vertex to start a search."""
import collections

class graph:
    def __init__(self, gd = None):
        if gd is None:
            gd = {}
        self.gd = gd


def bfs(graph, startn):
    seen, queue = set([startn]) , collections.deque([startn])
    while queue:
        vertex = queue.popleft()
        marked(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


def marked(n):
    print(n)

gd = { "a" : set(["b", "c"]),
           "b" : set(["a", "d"]),
           "c" : set(["a", "d"]),
           "d" : set(["e"]),
           "e" : set(["a"])
       }

bfs(gd, "e")
