import object.

class Essense(AbstractObject):
 
    def __init__(self, id, name, description, volatilityId, typeEssenseId):
        self.Id = id
        self.Name = name
        self.Description = description
        self.VolatilityId = volatilityId
        self.TypeEssenseId = typeEssenseId