import csv
from collections import defaultdict

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

def load_graph_from_csv(filepath_connections, filepath_stations):
    graph = Graph()
    from collections import defaultdict
    name_to_code = defaultdict(list)
    stations_by_name = defaultdict(list)

    with open(filepath_stations, newline='', encoding='utf-8') as stations_file:
        reader = csv.DictReader(stations_file)
        for row in reader:
            code = row["station_code"].strip()
            name = row["station_name"].strip()
            line = row["line"].strip()

            graph.add_station(code, name, line)
            name_to_code[name.lower()].append(code)
            name_to_code[code.lower()].append(code)
            stations_by_name[name].append(code)

    with open(filepath_connections, newline='', encoding='utf-8') as conn_file:
        reader = csv.DictReader(conn_file)
        for row in reader:
            from_name = row["From"].strip()
            to_name = row["To"].strip()
            time = int(row["Time"].strip())

            from_code = name_to_code.get(from_name.lower())
            to_code = name_to_code.get(to_name.lower())

            if from_code and to_code:
                graph.connect(from_code, to_code, time)

    for same_name_codes in stations_by_name.values():
        for i in range(len(same_name_codes)):
            for j in range(i + 1, len(same_name_codes)):
                graph.connect(same_name_codes[i], same_name_codes[j], 5)

    return graph, name_to_code
