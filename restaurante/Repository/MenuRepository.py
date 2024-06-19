import sqlite3
from db.db import bdata

db= bdata()

class MenuRepository:
    
    def __init__(self):
        self.conn=db.get_db()
        self.cursor= self.conn.cursor()

    def getCardapio(self,cursor):
        consulta=cursor.execute("SELECT * FROM cardapio").fetchall()
       
        return [dict(row) for row in consulta]
        
        
    def insertItemMenu(self,nome,valor):
        try:
            
            self.cursor.execute("INSERT INTO cardapio (nome,valor) VALUES (?, ?)",(nome,valor))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Invalid Insertion: {e}")
            return False
        
    def deleteItemMenu(self,id):
        try:
             
            self.cursor.execute("DELETE FROM cardapio WHERE id = ?",(id))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Invalid Insertion: {e}")
            return False

    
        
        
    
        
        