import math

# Simple Circle Class:

'''class Circle:
    def __init__(self, val, prop='r'):
        if prop == 'r':
            self.radius = val
        elif prop == 'd':
            self.radius = val / 2
        elif prop == 'c':
            self.radius = val / (2 * math.pi)
        elif prop == 'a':
            self.radius = (val / math.pi) ** .5
        else:
            raise Exception('prop must be r, d, c, or a')
        
        self.diameter = self.radius * 2
        self.circumference = self.radius * 2 * math.pi
        self.area = self.radius ** 2 * math.pi

c = Circle(10, 'd')
print(c.radius, c.diameter, c.circumference, c.area)'''

# Adding a Method:

'''class Circle:
    def __init__(self, val, prop='r'):
        if prop == 'r':
            self.radius = val
        elif prop == 'd':
            self.radius = val / 2
        elif prop == 'c':
            self.radius = val / (2 * math.pi)
        elif prop == 'a':
            self.radius = (val / math.pi) ** .5
        else:
            raise Exception('prop must be r, d, c, or a')
        
        self.diameter = self.radius * 2
        self.circumference = self.radius * 2 * math.pi
        self.area = self.radius ** 2 * math.pi
    
    def resize_by(self, amount):
        self.radius *= (1 + amount)
        self.diameter = self.radius * 2
        self.circumference = self.radius * 2 * math.pi
        self.area = self.radius ** 2 * math.pi
        
c = Circle(10, 'd')

c.resize_by(.2)
print(c.radius, c.diameter, c.circumference, c.area)

c.resize_by(-.5)
print(c.radius, c.diameter, c.circumference, c.area)'''

# Getters and Setters:

'''class Circle:
    def __init__(self, val, prop='r'):
        if prop == 'r':
            self.set_radius(val)
        elif prop == 'd':
            self.set_diameter(val)
        elif prop == 'c':
            self.set_circumference(val)
        elif prop == 'a':
            self.set_area(val)
        else:
            raise Exception('prop must be r, d, c, or a')
        
    def set_radius(self, r):
        self._radius = r
        self._diameter = r * 2
        self._circumference = r * 2 * math.pi
        self._area = r ** 2 * math.pi
    
    def get_radius(self):
        return self._radius
        
    def set_diameter(self, d):
        self.set_radius(d / 2)
    
    def get_diameter(self):
        return self._diameter
        
    def set_circumference(self, c):
        self.set_radius(c / (2 * math.pi))
        
    def get_circumference(self):
        return self._circumference
        
    def set_area(self, a):
        self.set_radius((a / math.pi) ** .5)
        
    def get_area(self):
        return self._area
    
    def resize_by(self, amount):
        r = self._radius * (1 + amount)
        self.set_radius(r)'''
        
'''c = Circle(10, 'd')
a = c.get_area()
print(a)

c.set_radius(8)
a = c.get_area()
print(a)

c = Circle(10, 'd')
a = c.get_area()
print(a)'''

# Set radius private variable directly (area will not be updated!):

'''c.radius = 8
a = c.get_area()
print(a)'''

# Using properties:

class Circle:
    def __init__(self, val, prop='r'):
        self._radius = None
        self._diameter = None
        self._circumference = None
        self._area = None
        if prop == 'r':
            self.radius = val
        elif prop == 'd':
            self.diameter = val
        elif prop == 'c':
            self.circumference = val
        elif prop == 'a':
            self.area = val
        else:
            raise Exception('prop must be r, d, c, or a')
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, r):
        self._radius = r
        self._diameter = r * 2
        self._circumference = r * 2 * math.pi
        self._area = r ** 2 * math.pi
    
    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, d):
        self.radius = d / 2
    
    @property
    def circumference(self):
        return self._circumference
    
    @circumference.setter
    def circumference(self, c):
        self.radius = c / (2 * math.pi)
    
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, a):
        self.radius = (a / math.pi) ** .5
    
    def resize_by(self, amount):
        self.radius = self.radius * (1 + amount)