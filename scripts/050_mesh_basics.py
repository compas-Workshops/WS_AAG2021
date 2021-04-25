import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

plotter = MeshPlotter(mesh, figsize=(8, 5))
plotter.draw_vertices()
plotter.draw_faces()
plotter.draw_edges()
plotter.show()