class Edge:
    def __init__(self, connection, weight):
        self.connection = connection
        self.weight = weight

class Vertex:
    def __init__(self, code, name, line):
        self.code = code
        self.name = name
        self.line = line
        self.edges = []
        self.color = 'white'
        self.distance = float('inf')
        self.parent = None

class Graph:
    def __init__(self):
        self.vertices = {}
        self.directed = False

    def add_station(self, code, name, line):
        if code not in self.vertices:
            self.vertices[code] = Vertex(code, name, line)

    def connect(self, code_a, code_b, weight):
        if code_a in self.vertices and code_b in self.vertices:
            va = self.vertices[code_a]
            vb = self.vertices[code_b]
            va.edges.append(Edge(vb, weight))
            if not self.directed:
                vb.edges.append(Edge(va, weight))

    def init_search(self):
        for v in self.vertices.values():
            v.color = 'white'
            v.distance = float('inf')
            v.parent = None

    def dijkstra(self, start_code):
        if start_code not in self.vertices:
            return False
        self.init_search()
        start = self.vertices[start_code]
        start.distance = 0
        queue = list(self.vertices.values())

        while queue:
            queue.sort(key=lambda v: v.distance)
            u = queue.pop(0)
            for edge in u.edges:
                v = edge.connection
                if u.distance + edge.weight < v.distance:
                    v.distance = u.distance + edge.weight
                    v.parent = u
        return True
