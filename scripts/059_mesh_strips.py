import compas
from compas.geometry import Scale, Translation
from compas.geometry import Point, Line
from compas.datastructures import Mesh
from compas_view2.app import App

tube = Mesh.from_off(compas.get('tubemesh.off'))
tube.update_default_face_attributes({'color': (0.8, 0.8, 0.8)})
loop = tube.edge_loop(next(tube.edges()))
for edge in loop[::2]:
    strip = tube.edge_strip(edge)
    for edge in strip:
        left, right = tube.edge_faces(*edge)
        if left is not None:
            tube.face_attribute(left, 'color', (0, 1, 0))
        if right is not None:
            tube.face_attribute(right, 'color', (0, 1, 0))

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