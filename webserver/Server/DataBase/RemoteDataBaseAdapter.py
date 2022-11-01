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
from object.combinationessense import CombinationEssense
from datetime import datetime

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

     query = "SELECT * FROM [dbo].[COMBINATION_ESSENSE]"
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       dataStorage.addCombinationEssense(CombinationEssense(item[0],item[2],item[3],item[1]))

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
    listWebPages.append(WebPages(item[0],item[2],item[1]))

  connection.close()
  return listWebPages

def getRecipeProfileById(id):
  mySqlServer = "DESKTOP-JH4MSCG\SQLEXPRESS"
  myDataBase = "WEB_SERVER_ESSENSE"
  connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+ mySqlServer +';'
                            'Database='+ myDataBase +';')
  dataStorage = DataStorage()
  curcor = connection.cursor()
  query = f'SELECT * FROM [dbo].[RECIPE_PROFILE] WHERE PROFILE_ID = {id}'
  curcor.execute(query)
  result = curcor.fetchall()
  for item in result:
    dataStorage.addRecipeProfile(RecipeProfile(item[0],item[1],item[2]))
  connection.close()
  return dataStorage.RecipeProfile

def getRecipe(id):
  mySqlServer = "DESKTOP-JH4MSCG\SQLEXPRESS"
  myDataBase = "WEB_SERVER_ESSENSE"
  connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+ mySqlServer +';'
                            'Database='+ myDataBase +';')

  curcor = connection.cursor()
  query = f'SELECT * FROM [dbo].[RECIPE] WHERE ID = {id}'
  curcor.execute(query)
  result = curcor.fetchall()
  for item in result:
    recipe = Recipe(item[0],item[1],item[2],item[3])

  connection.close()
  return recipe

def getCombinationEssense(id):
  mySqlServer = "DESKTOP-JH4MSCG\SQLEXPRESS"
  myDataBase = "WEB_SERVER_ESSENSE"
  connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+ mySqlServer +';'
                            'Database='+ myDataBase +';')
  dataStorage = DataStorage()
  curcor = connection.cursor()
  query = f'SELECT * FROM [dbo].[COMBINATION_ESSENSE] WHERE RECIPE_ID = {id}'
  curcor.execute(query)
  result = curcor.fetchall()
  for item in result:
    dataStorage.addCombinationEssense(CombinationEssense(item[0],item[2],item[3],item[1]))

  connection.close()
  return recipe

def getRecipes():
  mySqlServer = "DESKTOP-JH4MSCG\SQLEXPRESS"
  myDataBase = "WEB_SERVER_ESSENSE"
  connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+ mySqlServer +';'
                            'Database='+ myDataBase +';')

  dataStorage = DataStorage()
  curcor = connection.cursor()
  query = f'SELECT * FROM [dbo].[RECIPE]'
  curcor.execute(query)
  if len (dataStorage.Recipe) != 0:
    dataStorage.Recipe = []
  result = curcor.fetchall()
  for item in result:
    dataStorage.addRecipe(Recipe(item[0],item[1],item[2],item[3]))

  connection.close()
  return dataStorage.Recipe

def addOrder(name,surname,patronymic,mail,comment):
  mySqlServer = "DESKTOP-JH4MSCG\SQLEXPRESS"
  myDataBase = "WEB_SERVER_ESSENSE"
  connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+ mySqlServer +';'
                            'Database='+ myDataBase +';')

  curcor = connection.cursor()
  now = datetime.now()

  storedProc = "Exec [dbo].[Pr_REQUEST] @MAIL = 'wwww', @NAME = 'www', @SURNAME = 'wwww', @MIDDLE_NAME = 'ww', @COMMENT = 'www'"
  #params = (mail,name,surname,patronymic, comment)
  res = curcor.execute( storedProc) #params )
  row = curcor.fetchone()
  connection.close()


def insertRecipe(idProfile, name, chbx):
  mySqlServer = "DESKTOP-JH4MSCG\SQLEXPRESS"
  myDataBase = "WEB_SERVER_ESSENSE"
  connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+ mySqlServer +';'
                            'Database='+ myDataBase +';')

  curcor = connection.cursor()
  curcor.execute("""INSERT INTO anooog1 VALUES ([NAME], [VERIFICATION], [CHECKBOX])""",(name,0,chbx))
  curcor.execute(query)
  query = f'SELECT TOP 1 ID FROM [dbo].[RECIPE] ORDER BY ID DESC'
  result = curcor.fetchone()
  for item in result:
    id = item[0]
  query = f'INSERT INTO [dbo].[RECIPE_PROFILE] ([PROFILE_ID], [RECIPE_ID]) VALUES ({idProfile}, {id})'
  curcor.execute(query)
  connection.close()
  return id


def insertCombinationEssense(recipeId, oil, oilN):
  mySqlServer = "DESKTOP-JH4MSCG\SQLEXPRESS"
  myDataBase = "WEB_SERVER_ESSENSE"
  connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+ mySqlServer +';'
                            'Database='+ myDataBase +';')

  curcor = connection.cursor()
  query = f'INSERT INTO [dbo].[COMBINATION_ESSENSE] ([RECIPE_ID], [ESSENSE_NAME], [QUANTITY]) VALUES ({recipeId}, {oil}, {oilN})'
  curcor.execute(query)
  curcor.fetchone()
  query = f'SELECT TOP 1 ID FROM [dbo].[COMBINATION_ESSENSE] ORDER BY ID DESC'
  result = curcor.fetchone()
  connection.close()
  return id



