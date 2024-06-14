import sqlite3

DATABASE = 'restaurante_banco.db'

class MenuRepository:
    
    def __init__(self):
        self.conn=None
        
    def get_db(self):
        if self.conn is None or not self.conn:
           
            self.conn = sqlite3.connect(DATABASE)
            self.conn.row_factory = sqlite3.Row  # Retorna os resultados como dicionario
      
        return self.conn

    def close_db(self):
        if self.conn:
            self.conn.close()
            self.conn=None
    

    def getCardapio(self,cursor):
        consulta=cursor.execute("SELECT * FROM cardapio").fetchall()
       
        return [dict(row) for row in consulta]
        
        
    def insertItemMenu(self,cursor,nome,valor):
        try:
            cursor.execute("INSERT INTO cardapio (nome,valor) VALUES (?, ?)",(nome,valor))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Invalid Insertion: {e}")
            return False
        
    def deleteItemMenu(self,cursor,id):
        try:
            cursor.execute("DELETE FROM cardapio WHERE id = ?",(id))
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Invalid Insertion: {e}")
            return False

    
        
        
    
        
        