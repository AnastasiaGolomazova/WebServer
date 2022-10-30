from sqlite3 import connect
import pypyodbc
from datastorage import DataStorage
from object.essense import Essense

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
       essense = Essense(item[0],item[1],item[2],int(item[3]),int(item[4]))
       dataStorage.addEssense(essense)

     query = "SELECT * FROM [dbo].[EFFECT_ESSENSE]"
     dataStorage = DataStorage()
     curcor.execute(query)
     result = curcor.fetchall()
     for item in result:
       essense = Essense(item[0],item[1],item[2],int(item[3]),int(item[4]))
       dataStorage.addEffectEss(essense)

     connection.close()
