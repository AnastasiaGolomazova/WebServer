from sqlite3 import connect
import pypyodbc
from datastorage import DataStorage
from object.essense import Essense
from object.effect import Effect
from object.effectessense import EffectEssense
from object.profile import Profile
from object.recipe import Recipe
from object.recipeprofile import RecipeProfile
from object.steamessense import SteamEssense
from object.typeessense import TypeEssense
from object.volatity import Volatity
from object.webpages import WebPages

def getRequest():
     mySqlServer = "DESKTOP-JH4MSCG\SQLEXPRESS"
     myDataBase = "WEB_SERVER_ESSENSE"
     connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+ mySqlServer +';'
                            'Database='+ myDataBase +';')


     curcor = connection.cursor()

     query = "SELECT * FROM [dbo].[ESSENSE]"
     dataStorage = DataStorage()
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       dataStorage.addEssense(Essense(item[0],item[1],item[2],int(item[3]),int(item[4])))

     query = "SELECT * FROM [dbo].[EFFECT]"
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       dataStorage.addEffect(Effect(item[0],item[1]))

     query = "SELECT * FROM [dbo].[EFFECT_ESSENSE]"
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       dataStorage.addEffectEssense(EffectEssense(item[0],item[1],item[2]))
    
     query = "SELECT * FROM [dbo].[PROFILE]"
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       dataStorage.addProfile(Profile(item[0],item[1],item[2]))

     query = "SELECT * FROM [dbo].[RECIPE]"
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       dataStorage.addRecipe(Recipe(item[0],item[1]))

     query = "SELECT PROFILE_ID, RECIPE_ID FROM [dbo].[RECIPE_PROFILE]"
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       dataStorage.addRecipeProfile(RecipeProfile(item[0],item[1]))

     query = "SELECT ESSENSE1_ID, ESSENSE2_ID FROM [dbo].[STEAM_ESSENSE]"
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       dataStorage.addSteamEssense(SteamEssense(item[0],item[1]))

     query = "SELECT * FROM [dbo].[TYPE_ESSENSE]"
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       dataStorage.addTypeEssense(TypeEssense(item[0],item[1]))

     query = "SELECT * FROM [dbo].[VOLATILITY]"
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       dataStorage.addVolatity(Volatity(item[0],item[1]))

     

     connection.close()


def getRequestPage():
  mySqlServer = "DESKTOP-JH4MSCG\SQLEXPRESS"
  myDataBase = "WEB_SERVER_ESSENSE"
  connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+ mySqlServer +';'
                            'Database='+ myDataBase +';')


  curcor = connection.cursor()
  query = "SELECT * FROM [dbo].[WEB_PAGES]"
  curcor.execute(query)
  result = curcor.fetchall()
  listWebPages = []
  for item in result:
    listWebPages.append(WebPages(item[0],item[1]))

  connection.close()
  return listWebPages
