import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

vertex = mesh.get_any_vertex()
vertex_nbrs = mesh.vertex_neighbors(vertex)

face = mesh.get_any_face()
face_nbrs = mesh.face_neighbors(face)

vertexcolor = {vertex: (255, 0, 0)}
for nbr in vertex_nbrs:
    vertexcolor[nbr] = (0, 0, 255)

edgecolor = {}
for nbr in vertex_nbrs:
    edgecolor[vertex, nbr] = (0, 255, 0)
    edgecolor[nbr, vertex] = (0, 255, 0)

facecolor = {face: (255, 0, 0)}
for nbr in face_nbrs:
    facecolor[nbr] = (0, 0, 255)

plotter = MeshPlotter(mesh, figsize=(8, 5))
plotter.draw_vertices(facecolor=vertexcolor)
plotter.draw_faces(facecolor=facecolor)
plotter.draw_edges(color=edgecolor, width={edge: 2.0 for edge in edgecolor})
plotter.show()