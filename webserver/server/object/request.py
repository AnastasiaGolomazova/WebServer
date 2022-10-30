from object.abstractobject import AbstractObject

class Recipe(AbstractObject):
 
    def __init__(self, id, mail, profileId, time):
        AbstractObject.__init__(self, id,'')
        self.Mail =  mail
        self.ProfileId=  profileId
        self.Time =  time