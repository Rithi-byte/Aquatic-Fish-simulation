from flask import Flask, render_template, jsonify
import random
import heapq
import networkx as nx

app = Flask(__name__)

graph = nx.grid_2d_graph(20, 20)

for (u, v) in graph.edges():
    graph.edges[u, v]['weight'] = 1

food_sources = [(random.randint(0, 19), random.randint(0, 19)) for _ in range(5)]
pollutants = []

def add_pollutant(level, name):
    heapq.heappush(pollutants, (level, name))

class Fish:
    def __init__(self, id):
        self.id = id
        self.x = random.randint(0, 19)
        self.y = random.randint(0, 19)
        self.energy = random.randint(50, 100)

    def move(self):
        global food_sources
        if self.energy < 50 and food_sources:
            nearest_food = min(food_sources, key=lambda food: dijkstra_distance((self.x, self.y), food))
            path = nx.dijkstra_path(graph, source=(self.x, self.y), target=nearest_food, weight='weight')
            if len(path) > 1:
                self.x, self.y = path[1]
            if (self.x, self.y) == nearest_food:
                self.energy = min(100, self.energy + 30)
                food_sources.remove(nearest_food)
                food_sources.append((random.randint(0, 19), random.randint(0, 19)))
        else:
            neighbors = list(graph.neighbors((self.x, self.y)))
            if neighbors:
                self.x, self.y = random.choice(neighbors)
        self.energy -= 1
        if self.energy <= 0:
            self.x = random.randint(0, 19)
            self.y = random.randint(0, 19)
            self.energy = random.randint(50, 100)

def dijkstra_distance(start, goal):
    try:
        return nx.dijkstra_path_length(graph, source=start, target=goal, weight='weight')
    except nx.NetworkXNoPath:
        return float('inf')

fish_population = [Fish(i) for i in range(10)]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fish_data")
def fish_data():
    for fish in fish_population:
        fish.move()
    return jsonify([{"id": fish.id, "x": fish.x, "y": fish.y, "energy": fish.energy} for fish in fish_population])

@app.route("/food_data")
def food_data_route():
    return jsonify(food_sources)

@app.route("/add_pollutant/<int:level>/<name>")
def add_pollutant_route(level, name):
    add_pollutant(level, name)
    return jsonify({"message": f"Pollutant '{name}' with level {level} added."})

@app.route("/get_pollutants")
def get_pollutants():
    return jsonify({"pollutants": pollutants})

if __name__ == "__main__":
    app.run(debug=True)