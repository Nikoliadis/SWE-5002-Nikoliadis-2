class GraphData:
    def __init__(self):
        self.graph = {}

    def add_station(self, station_name):
        if station_name not in self.graph:
            self.graph[station_name] = []
        
    def add_connections(self, from_station, to_station, line, time):
        self.add_station(from_station)
        self.add_station(to_station)
        self.graph[from_station].append((to_station, line, time))
        self.graph[to_station].append((from_station, line, time))

    def get_connections(self, station_name):
        return self.graph.get(station_name, [])
    
    def get_stations(self):
        return list(self.graph.keys())