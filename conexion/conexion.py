#conexion a mysql
import mysql.connector
from mysql.connector import Error 
def get_connection():
   try: 
     
      connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mmzm1996",
        database="bolis_db"
    )
      if connection.is_connected():
       return connection
   except Error as e:
     print( f"error al conectar a MySQL:{e}") 
     return None
