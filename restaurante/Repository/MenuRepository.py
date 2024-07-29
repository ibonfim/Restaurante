import sqlite3
from db.db import bdata
from class_models.Class_models import Cardapio


db= bdata()

class MenuRepository:
    
    def __init__(self):
        self.conn=db.get_db()
        self.cursor= self.conn.cursor()

    def getCardapio(self,cursor):
        consulta=cursor.execute("SELECT * FROM cardapio").fetchall()
       
        return [dict(row) for row in consulta]
        
        
    def insertItemMenu(self,cardapio:Cardapio):
        try:
            
            self.cursor.execute("INSERT INTO cardapio (nome,valor) VALUES (?, ?)",(cardapio.nome,cardapio.valor))
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

    
        
        
    
        
        