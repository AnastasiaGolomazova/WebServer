from object.abstractobject import AbstractObject

class Essense(AbstractObject):
 
    def __init__(self, id, name, description, volatilityId, typeEssenseId):
        AbstractObject.__init__(self, id, name)
        self.Description = description
        self.VolatilityId = volatilityId
        self.TypeEssenseId = typeEssenseId