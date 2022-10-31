from object.abstractobject import AbstractObject

class Recipe(AbstractObject):
 
    def __init__(self, id, name, verification, checkbox):
        AbstractObject.__init__(self, id, name)
        self.Verification = verification
        self.Checkbox = checkbox

    def toJson(self):
       return f'{{"name" : {self.Name}}}'