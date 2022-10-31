from object.abstractobject import AbstractObject

class SteamEssense(AbstractObject):
 
    def __init__(self, id, essense1Id, essense2Id):
        AbstractObject.__init__(self, id, '')
        self.Essense1Id = essense1Id
        self.Essense2Id = essense2Id

    def toJson(self):
        return f'{{"essense1Id" : {self.Essense1Id}, "essense2Id" : "{self.Essense2Id}"}}'