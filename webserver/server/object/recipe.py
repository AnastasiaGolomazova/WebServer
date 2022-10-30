from object.abstractobject import AbstractObject

class Recipe(AbstractObject):
 
    def __init__(self, id, name):
        AbstractObject.__init__(self, id, name)