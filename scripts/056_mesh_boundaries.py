from random import choice
import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))
vertex = choice(list(set(mesh.vertices()) - set(mesh.vertices_on_boundary())))
mesh.delete_vertex(vertex)
mesh.remove_unused_vertices()

boundaries = mesh.vertices_on_boundaries()

print(boundaries)

plotter = MeshPlotter(mesh, figsize=(8, 5))
plotter.draw_vertices(
    facecolor={vertex: (255, 0, 0) for boundary in boundaries for vertex in boundary},
    text={vertex: index for index, vertex in enumerate(boundaries[0])},
    radius={vertex: 0.3 for vertex in boundaries[0]}
)
plotter.draw_faces()
plotter.draw_edges()
plotter.show()