
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataStorage(metaclass = Singleton):
    __instance = None

    def __init__(self):
        self.Essense = []
        self.TypeProfile = []
        self.TypeEssense  = []
        self.EffectEssense  = []
        self.Recipe = []
        self.Effect = []
        self.Volatity = []
        self.Profile = []
        self.SteamEssense = []
        self.RecipeProfile = []


    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = DataStorage()
        return cls.__instance

    def addEssense(self, essense):
        self.Essense.append(essense)

    def addRecipeProfile(self, recipeProfile):
        self.RecipeProfile.append(recipeProfile)

    def addEffectEssense(self, effectEssense):
        self.EffectEssense.append(effectEssense)

    def addTypeProfile(self, typeProfile):
        self.TypeProfile.append(typeProfile)

    def addRecipe (self, typeEssense):
        self.TypeEssense.append(typeEssense)

    def addTypeEssense(self, recipe):
        self.Recipe.append(recipe)

    def addEffect(self, effect):
        self.Effect.append(effect)

    def addVolatity (self, volatity):
        self.Volatity.append(volatity)

    def addProfile(self, profile):
        self.Profile.append(profile)

    def addSteamEssense (self, steamEssense):
        self.SteamEssense.append(steamEssense)


    def getEssense(self, id):
        for i in self.Essense:
            if i.Id == id:
                return i
        return False

    def getEffectEssense(self, id):
        for i in self.EffectEssense:
            if i.Id == id:
                return i
        return False


    def getTypeProfile(self, id):
        for i in self.TypeProfile:
            if i.Id == id:
                return i
        return False

    def getRecipe (self, id):
        for i in self.Recipe:
            if i.Id == id:
                return i
        return False

    def getTypeEssense(self, id):
        for i in self.TypeEssense:
            if i.Id == id:
                return i
        return False

    def getVolatity (self, id):
        for i in self.Volatity:
            if i.Id == id:
                return i
        return False

    def getProfile(self, id):
        for i in self.Profile:
            if i.Id == id:
                return i
        return False

    def getSteamEssense (self, id):
        for i in self.SteamEssense:
            if i.Id == id:
                return i
        return False
        
    def getEffect(self, id):
       for i in self.Effect:
            if i.Id == id:
                return i