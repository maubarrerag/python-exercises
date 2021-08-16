from FlyingObject import FlyingObject

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