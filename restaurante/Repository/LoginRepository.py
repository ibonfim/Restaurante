    
from db.db import bdata
from class_models.Class_models import UserLogin
from fastapi import FastAPI, HTTPException, Depends, status

db= bdata()


class LoginRepository:
       
    def __init__(self):
        self.conn=db.get_db()
        self.cursor= self.conn.cursor()
        
    def selectUser(self,user:UserLogin):
        user=self.cursor.execute("SELECT * FROM user WHERE nome= ? AND senha=?", (user.username,user.password)).fetchone()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciais inválidas",
                headers={"WWW-Authenticate": "Basic"},
            )
        
        return user
            
    
