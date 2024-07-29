import sqlite3
from db.db import bdata
from class_models.Class_models import User

db= bdata()


class UserRepository:
    
    def __init__(self):
        self.conn=db.get_db()
        self.cursor= self.conn.cursor()
            

    def getAllUsers(self,cursor):
        cursor = self.conn.cursor()
        consulta=cursor.execute("SELECT nome,endereco,telefone FROM user ").fetchall()
        return consulta
        
        
    def insertUser(self,user:User):
        try:
            
            self.cursor.execute("INSERT INTO user (nome,cpf,endereco,telefone,senha,usertype) VALUES (?,?,?,?,?,?)",(user.nome,user.CPF,user.endereco,user.telefone,user.senha,user.usertype))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Invalid User Insertion: {e}")
            return False
        
            
    def deleteUser(self,id):
        try:
             
            self.cursor.execute("DELETE FROM user WHERE id = ?",(id))
            self.conn.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Invalid Insertion: {e}")
            return False


 