# Test subclassing abstract super class:

import abc

from FlyingObject import FlyingObject

#ufo = FlyingObject()  # cannot instantiate abstract class
#print(FlyingObject.num_objects())

# Improper sublcass (lacks implementation of abstract "land" method):

'''class Plane(FlyingObject):
    
    @property
    def pilot_awake(self):
        return True
    def take_off(self):
        if self.pilot_awake:
            super().take_off()
        self._in_air = True'''

#plane = Plane()   # Will fail at runtime

# Proper subclass of FlyingObject:

class Plane(FlyingObject):
    
    @property
    def pilot_awake(self):
        return True
    @property
    def over_land(self):
        return True    
    def take_off(self):
        if self.pilot_awake:
            super().take_off()
        self._in_air = True
    def land(self):
        if self.over_land:
            super().land()    

#plane = Plane() 
#print(FlyingObject.num_objects())  

# Bird class:

class Bird(FlyingObject):
    
    @property
    def healthy_wings(self):
        return True   
    def take_off(self):
        if self.healthy_wings:
            super().take_off()
        self._in_air = True
    def land(self):
        super().land() 

bird = Bird()
bird.take_off()
print(FlyingObject.num_objects(), FlyingObject.num_objects_in_air())