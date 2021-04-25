import compas
from compas.geometry import Scale, Translation
from compas.geometry import Point, Line
from compas.datastructures import Mesh
from compas_view2.app import App

tube = Mesh.from_off(compas.get('tubemesh.off'))
loop = tube.edge_loop(next(tube.edges()))

centroid = tube.centroid()
S = Scale.from_factors([0.5, 0.5, 0.5])
T = Translation.from_vector(Point(0, 0, 0) - Point(centroid[0], centroid[1], 0))

tube.transform(S * T)

viewer = App()

viewer.add(tube, show_edges=True)
for edge in loop:
    a, b = tube.edge_coordinates(*edge)
    line = Line(a, b)
    viewer.add(line, linewidth=10, linecolor=(1, 0, 0))

viewer.run()