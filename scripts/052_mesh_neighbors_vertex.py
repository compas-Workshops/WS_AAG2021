import compas
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

mesh = Mesh.from_obj(compas.get('faces.obj'))

vertex = mesh.get_any_vertex()
nbrs = mesh.vertex_neighbors(vertex, ordered=True)

vertexcolor = {vertex: (255, 0, 0)}
for nbr in nbrs:
    vertexcolor[nbr] = (0, 0, 255)

edgecolor = {}
for nbr in nbrs:
    edgecolor[vertex, nbr] = (0, 255, 0)
    edgecolor[nbr, vertex] = (0, 255, 0)

plotter = MeshPlotter(mesh, figsize=(8, 5))
plotter.draw_vertices(
    facecolor=vertexcolor,
    radius=0.2,
    text={vertex: str(index) for index, vertex in enumerate(nbrs)},
    textcolor=(1, 1, 1))
plotter.draw_faces()
plotter.draw_edges(color=edgecolor, width={edge: 2.0 for edge in edgecolor})
plotter.show()