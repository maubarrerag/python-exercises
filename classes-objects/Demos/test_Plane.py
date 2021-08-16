# Test Plane class:

from Plane import Plane

p1 = Plane()
p2 = Plane()
p3 = Plane()
p1.take_off()
p2.take_off()
p1.land()
print(Plane.num_planes(), Plane.num_planes_in_air())