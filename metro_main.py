import csv
from metro_loader import load_graph_from_csv
from metro_graph import Graph


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

def display_csv(filepath):
    print("\nMRT Connections from CSV:")
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(" | ".join(row))

def display_stations(filepath):
    print("\nStation List:")
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(" | ".join(row))

def reconstruct_path(end_vertex):
    path = []
    current = end_vertex
    while current:
        path.append(current.name)
        current = current.parent
    return list(reversed(path))

def main():
    graph, name_to_code = load_graph_from_csv("mrt_connections.csv", "stations.csv")

    while True:
        print("\nSingapore MRT Route Finder")
        print("1. Find shortest path (fewest stops)")
        print("2. Find fastest route (least time)")
        print("3. Display MRT connections")
        print("4. Display station list")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1" or choice == "2":
            start_name = input("Enter start station name: ").strip().lower()
            end_name = input("Enter destination station name: ").strip().lower()

            start_code = name_to_code.get(start_name)
            end_code = name_to_code.get(end_name)

            if not start_code or not end_code:
                print("Station name not found. Please check and try again.")
                continue

            graph.dijkstra(start_code)
            end_vertex = graph.vertices[end_code]
            if end_vertex.distance == float("inf"):
                print("No path found.")
            else:
                path = reconstruct_path(end_vertex)
                print("\nShortest path:" if choice == "1" else "\nFastest path:")
                print(" → ".join(path))
                print(f"Total travel time: {end_vertex.distance} minutes")

        elif choice == "3":
            display_csv("mrt_connections.csv")
        elif choice == "4":
            display_stations("stations.csv")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
