from graph_data import GraphData

def main():
    graph = GraphData()

    graph.add_connections("Dhoby Ghaut", "City Hall", "North South Line", 3)
    graph.add_connections("City Hall", "Raffles Place", "North South Line", 2)
    graph.add_connections("Raffles Place", "Marina Bay", "North South Line", 4)
    graph.add_connections("Dhoby Ghaut", "Bras Basah", "Circle Line", 5)
    graph.add_connections("Bras Basah", "Esplanade", "Circle Line", 2)

    for station in graph.get_stations():
        print(f"\n{station} connects to:")
        for conn in graph.get_connections(station):
            print(f"  → {conn[0]} via {conn[1]} line ({conn[2]} min)")

if __name__ == "__main__":
    main()