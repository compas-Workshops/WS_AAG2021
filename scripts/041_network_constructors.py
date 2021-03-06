import compas
from compas.datastructures import Network
from compas_plotters import NetworkPlotter

network = Network.from_obj(compas.get('grid_irregular.obj'))

plotter = NetworkPlotter(network, figsize=(8, 5))
plotter.draw_nodes()
plotter.draw_edges()
plotter.show()
