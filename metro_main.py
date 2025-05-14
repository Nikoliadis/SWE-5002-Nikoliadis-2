import csv
from metro_loader import load_graph_from_csv

def display_csv(filepath):
    print("\n📄 MRT Connections:")
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(" | ".join(row))

def display_stations(filepath):
    print("\n📍 MRT Station List:")
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Skip header
        for row in reader:
            print(" | ".join(row))

def main():
    graph = load_graph_from_csv("mrt_connections.csv")

    while True:
        print("\nSingapore MRT Route Finder")
        print("1. Find shortest path (fewest stops)")
        print("2. Find fastest route (least time)")
        print("3. Display MRT connections")
        print("4. Display MRT stations")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            start = input("Enter start station name: ")
            end = input("Enter destination station name: ")
            path = graph.shortest_path(start, end)
            if path:
                print("\nShortest path:")
                print(" → ".join(path))
            else:
                print("No path found.")

        elif choice == "2":
            start = input("Enter start station name: ")
            end = input("Enter destination station name: ")
            path, time = graph.fastest_path(start, end)
            if path:
                print("\nFastest path:")
                print(" → ".join(path))
                print(f"Total travel time: {time} minutes")
            else:
                print("No path found.")

        elif choice == "3":
            display_csv("mrt_connections.csv")

        elif choice == "4":
            display_stations("station_list.csv")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
