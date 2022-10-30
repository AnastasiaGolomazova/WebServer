from object.abstractobject import AbstractObject

class EffectEssense(AbstractObject):
 
    def __init__(self, id, essenseId, effectId):
        AbstractObject.__init__(self, id, '')
        self.EsseneId = essenseId
        self.EffectId = effectId