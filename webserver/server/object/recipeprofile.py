from object.abstractobject import AbstractObject

class RecipeProfile(AbstractObject):
 
    def __init__(self, profileId, recipeId):
        AbstractObject.__init__(self, 0, '')
        self.ProfileId = profileId
        self.RecipeId = recipeId



    def toJson(self):
       return f'{{"essense1Id" : {self.Essense1Id}, "essense2Id" : "{self.Essense2Id}"}}'