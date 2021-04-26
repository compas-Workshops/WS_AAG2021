import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

face = mesh.get_any_face()
nbrs = mesh.face_neighbors(face)

facecolor = {face: (255, 0, 0)}
for nbr in nbrs:
    facecolor[nbr] = (0, 0, 255)

plotter = MeshPlotter(mesh, figsize=(8, 5))
plotter.draw_vertices()
plotter.draw_faces(facecolor=facecolor)
plotter.draw_edges()
plotter.show()