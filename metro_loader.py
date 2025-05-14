from metro_graph import Graph
import csv
from collections import defaultdict

def load_graph_from_csv(filepath_connections, filepath_stations):
    graph = Graph()
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
            from_station = row["From"].strip().lower()
            to_station = row["To"].strip().lower()
            time = int(row["Time"].strip())

            from_codes = name_to_code.get(from_station, [])
            to_codes = name_to_code.get(to_station, [])

            for from_code in from_codes:
                for to_code in to_codes:
                    graph.connect(from_code, to_code, time)

    for codes in stations_by_name.values():
        for i in range(len(codes)):
            for j in range(i + 1, len(codes)):
                graph.connect(codes[i], codes[j], 5)

    return graph, name_to_code
