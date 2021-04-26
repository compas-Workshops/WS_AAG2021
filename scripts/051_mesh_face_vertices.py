from random import choice
import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

face = mesh.get_any_face()
vertices = mesh.face_vertices(face)

plotter = MeshPlotter(mesh, figsize=(8, 5))
plotter.draw_vertices(
    text={vertex: index for index, vertex in enumerate(vertices)},
    radius=0.2
)
plotter.draw_faces(facecolor={face: (255, 0, 0)})
plotter.draw_edges()
plotter.show()