from sqlite3 import connect
import pypyodbc

mySqlServer = "DESKTOP-JH4MSCG\SQLEXPRESS"
myDataBase = "WEB_SERVER_ESSENSE"
connection = pypyodbc.connect('Driver={SQL Server};'
                            'Server='+ mySqlServer +';'
                            'Database='+ myDataBase +';')


curcor = connection.cursor()



Query = "SELECT * FROM [dbo].[EFFECT_ESSENSE]"

curcor.execute(Query)
result = curcor.fetchall()
print(result)
connection.close()