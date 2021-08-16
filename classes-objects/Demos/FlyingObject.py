import abc

class FlyingObject(metaclass=abc.ABCMeta):
    flyingobjects = []
    def __init__(self):
        self._in_air = False
        type(self).flyingobjects.append(self)
    
    @abc.abstractmethod
    def take_off(self):
        self._in_air = True
    
    @abc.abstractmethod
    def land(self):
        self._in_air = False
    
    @classmethod
    def num_objects(cls):
        return len(cls.flyingobjects)
    
    @classmethod
    def num_objects_in_air(cls):
        return len([fo for fo in cls.flyingobjects if fo._in_air])