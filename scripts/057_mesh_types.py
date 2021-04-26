from math import radians
import compas
from compas.geometry import Scale, Translation, Rotation, Frame
from compas.geometry import Point
from compas.datastructures import Mesh
from compas_view2.app import App

faces = Mesh.from_obj(compas.get('faces.obj'))

tube = Mesh.from_off(compas.get('tubemesh.off'))
centroid = tube.centroid()
S = Scale.from_factors([0.5, 0.5, 0.5], Frame(centroid, [1, 0, 0], [0, 1, 0]))
T = Translation.from_vector(Point(15, 0, 0) - Point(centroid[0], centroid[1], 0))
tube.transform(T * S)

polyhedron = Mesh.from_polyhedron(12)
polyhedron.transform(Scale.from_factors([3, 3, 3]))

bunny = Mesh.from_ply(compas.get_bunny())
bunny.cull_vertices()

T1 = Translation.from_vector(Point(0, 0, 0) - Point(* bunny.centroid()))
S = Scale.from_factors([100, 100, 100])
R = Rotation.from_axis_and_angle([1, 0, 0], radians(90))
T2 = Translation.from_vector(Point(-15, 10, 0))

bunny.transform(T2 * R * S * T1)

viewer = App()
viewer.add(faces, show_edges=True)
viewer.add(tube, show_edges=True)
viewer.add(bunny, show_edges=True)
viewer.add(polyhedron, show_edges=True)
viewer.run()