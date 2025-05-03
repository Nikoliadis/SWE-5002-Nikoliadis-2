import csv
import random
from graph_data import GraphData

def load_graph_from_csv(filepath):
    graph = GraphData()

    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            from_station = row['From']
            to_station = row['To']
            line = row['Line']
            time = random.randint(2, 8)

            graph.add_connections(from_station, to_station, line, time)

    return graph