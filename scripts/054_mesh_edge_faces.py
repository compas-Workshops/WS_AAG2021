from random import choice
import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))
edge = choice(list(mesh.edges()))

left, right = mesh.edge_faces(*edge)

plotter = MeshPlotter(mesh, figsize=(8, 5))
plotter.draw_vertices(
    text={vertex: str(index) for index, vertex in enumerate(edge)},
    radius={vertex: 0.2 for vertex in edge},
    facecolor={vertex: (255, 0, 0) for vertex in edge}
)
plotter.draw_faces(
    facecolor={left: (0, 255, 255), right: (0, 0, 255)}
)
plotter.draw_edges(
    color={edge: (0, 255, 0)}
)
plotter.show()