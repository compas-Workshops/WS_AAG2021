import compas
from compas.datastructures import Network
from compas_plotters import NetworkPlotter

network = Network()

a = network.add_node(x=0, y=0)
b = network.add_node(x=1, y=0)
c = network.add_node(x=0, y=1)
d = network.add_node(x=-1, y=0)
e = network.add_node(x=0, y=-1)

network.add_edge(a, b)
network.add_edge(a, c)
network.add_edge(a, d)
network.add_edge(a, e)

print(network)

print(network.nodes())
print(network.edges())

# plotter = NetworkPlotter(network, figsize=(8, 5))
# plotter.draw_nodes()
# plotter.draw_edges()
# plotter.show()
