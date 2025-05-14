import csv
from metro_graph import Graph


def load_graph_from_csv(filepath_connections, filepath_stations):
    graph = Graph()
    name_to_code = {}

    with open(filepath_stations, newline='', encoding='utf-8') as stations_file:
        reader = csv.DictReader(stations_file)
        for row in reader:
            code = row["station_code"].strip()
            name = row["station_name"].strip()
            line = row["line"].strip()
            graph.add_station(code, name, line)
            name_to_code[name.lower()] = code
            name_to_code[code.lower()] = code 


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

    return graph, name_to_code
