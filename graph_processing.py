import networkx as nx

G = nx.Graph()

# Kameraları düğümler olarak ekle
vehicles = [f"Car{i}" for i in range(2, 11)]
for vehicle in vehicles:
    G.add_node(vehicle)

# Kenarları (bağlantıları) ekle
edges = [
    ("Car2", "Car3"),
    ("Car3", "Car4"),
    ("Car3", "Car6"),
    ("Car4", "Car5"),
    ("Car6", "Car7"),
    ("Car6", "Car8"),
    ("Car8", "Car9"),
    ("Car9", "Car10")
]

G.add_edges_from(edges)
