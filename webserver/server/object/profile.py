from object.abstractobject import AbstractObject

class Profile(AbstractObject):
 
    def __init__(self, id, name, password):
        AbstractObject.__init__(self, id, name)
        self.Password = password