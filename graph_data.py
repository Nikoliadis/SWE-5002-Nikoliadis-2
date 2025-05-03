from collections import deque
import heapq

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

    def shortest_path(self, start, goal):
        visited = set()
        queue = deque([(start, [start])])

        while queue:
            current_station, path = queue.popleft()
            if current_station == goal:
                return path

            if current_station not in visited:
                visited.add(current_station)
                for neighbor, line, time in self.graph.get(current_station, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))

        return None

    def fastest_path(self, start, goal):
        queue = [(0, start, [start], None)]  # (total_time, current_station, path, current_line)
        visited = {}

        while queue:
            time_so_far, current, path, prev_line = heapq.heappop(queue)

            if current == goal:
                return path, time_so_far

            if current in visited and visited[current] <= time_so_far:
                continue
            visited[current] = time_so_far

            for neighbor, line, t in self.graph.get(current, []):
                extra = 5 if prev_line and line != prev_line else 0
                heapq.heappush(queue, (
                    time_so_far + t + extra,
                    neighbor,
                    path + [neighbor],
                    line
                ))

        return None, float("inf")