from random import choice
import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

vertex = choice(list(set(mesh.vertices()) - set(mesh.vertices_on_boundary())))
nbrs = mesh.vertex_neighbors(vertex, ordered=True)
faces = mesh.vertex_faces(vertex, ordered=True)

plotter = MeshPlotter(mesh, figsize=(8, 5))
plotter.draw_vertices(facecolor={vertex: (255, 0, 0)}, text={vertex: index for index, vertex in enumerate(nbrs)}, radius=0.2)
plotter.draw_faces(text={face: str(index) for index, face in enumerate(faces)})
plotter.draw_edges()
plotter.show()