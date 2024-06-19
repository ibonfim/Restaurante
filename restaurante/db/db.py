  
import sqlite3

DATABASE = 'restaurante_banco.db'

class bdata:
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
            
    
                

        
        

                
                