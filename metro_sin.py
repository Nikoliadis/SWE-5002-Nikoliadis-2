from metro_loader import load_graph_from_csv

def main():
    graph = load_graph_from_csv("mrt_connections.csv")

    print("\nStations loaded:")
    for station in graph.get_stations():
        print(f"  {station}")

    path = graph.shortest_path("Dhoby Ghaut", "Marina Bay")
    if path:
        print("\nShortest path:")
        print(" → ".join(path))
    else:
        print("No shortest path found.")

    fastest_path, time = graph.fastest_path("Dhoby Ghaut", "Marina Bay")
    if fastest_path:
        print("\nFastest path:")
        print(" → ".join(fastest_path))
        print(f"Total travel time: {time} minutes")
    else:
        print("No fastest path found.")

if __name__ == "__main__":
    main()