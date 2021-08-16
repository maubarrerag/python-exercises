# Test Bird class:

from FlyingObject import FlyingObject
from Bird import Bird

bird = Bird()
bird.take_off()
print(FlyingObject.num_objects(), FlyingObject.num_objects_in_air())