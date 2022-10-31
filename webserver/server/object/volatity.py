from object.abstractobject import AbstractObject

class Volatity(AbstractObject):
 
    def __init__(self, id, name):
        AbstractObject.__init__(self, id, name)

    def toJson(self):
        return f'{{"id" : {self.Id}, "name" : "{self.Name}"}}'