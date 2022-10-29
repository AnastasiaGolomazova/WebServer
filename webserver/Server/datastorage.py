import Object.essense as Essense

class DataStorage:
    __instance = None

    def __init__(self):
        self.Essense = []
        self.TypeProfile = []
        self.TypeEssense  = []
        self.Recipe = []
        self.Effect = []
        self.Volatity = []
        self.Profile = []
        self.SteamEssense = []


    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = DataStorage()
        return cls.__instance

    def addEssense(self, essense):
        self.Essense.Add(essense)

    def addTypeProfile(self, typeProfile):
        self.TypeProfile.Add(typeProfile)

    def addRecipe (self, typeEssense):
        self.TypeEssense.Add(typeEssense)

    def addTypeEssense(self, recipe):
        self.Recipe.Add(recipe)

    def addEffect(self, effect):
        self.Effect.Add(effect)

    def addVolatity (self, volatity):
        self.Volatity.Add(volatity)

    def addProfile(self, profile):
        self.Profile.Add(profile)

    def addSteamEssense (self, steamEssense):
        self.SteamEssense.Add(steamEssense)


    def getEssense(self, id):
        for i in self.Essense:
            if i.Id == id:
                return i

    def getTypeProfile(self, id):
        for i in self.TypeProfile:
            if i.Id == id:
                return i

    def getRecipe (self, id):
        for i in self.Recipe:
            if i.Id == id:
                return i

    def getTypeEssense(self, id):
        for i in self.TypeEssense:
            if i.Id == id:
                return i

    def getEffect(self, id):
       for i in self.Effect:
            if i.Id == id:
                return i

    def getVolatity (self, id):
        for i in self.Volatity:
            if i.Id == id:
                return i

    def getProfile(self, id):
        for i in self.Profile:
            if i.Id == id:
                return i

    def getSteamEssense (self, id):
        for i in self.SteamEssense:
            if i.Id == id:
                return i
        