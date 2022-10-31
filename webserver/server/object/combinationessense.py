from object.abstractobject import AbstractObject

class CombinationEssense(AbstractObject):
 
    def __init__(self, id, name, quantity, recipeId):
        AbstractObject.__init__(self, id, name)
        self.Quantity = quantity
        self.RecipeId = recipeId