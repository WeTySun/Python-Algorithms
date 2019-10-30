# Intermediate level of displaying graph in python
class graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findedges()


    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

    def addVertex(self,vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def addEdge(self,edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

graph_elements = { "a" : ["b","c"],
                   "b" : ["a","d"],
                   "c" : ["a", "d"],
                   "d" : ["e"],
                   "e" : ["d"]
                   }

g = graph(graph_elements)


print(g.getVertices())
print(g.edges())
g.addVertex("f")
print("After adding vertex: " + str(g.getVertices()))
g.addEdge({'a','e'})
g.addEdge({'a','c'})
print("After adding edge: " + str(g.edges()))
