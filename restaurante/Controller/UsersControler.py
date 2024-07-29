import sys
import os
from fastapi import APIRouter, Body, HTTPException
# Adicione o diretório principal ao sys.path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Repository.UserRepository import UserRepository
from db.db import bdata
from class_models.Class_models import User

db=bdata()
userRepository= UserRepository()

router = APIRouter()



@router.get("/users")
async def get_users():
    conn=db.get_db()
    cursor=conn.cursor()
    try:
        user=userRepository.getAllUsers(cursor)
        if user:
            return   user
        else:
            raise HTTPException(status_code=404, detail="User not found")
    finally:
        db.close_db()
        
        
#Delegar apenas para admin qdo autenticação tiver pronta        
@router.post("/insertuser")
async def insert_menu(user: User = Body(...)):
    
    try:
        if userRepository.insertUser(user):
            return "Created User"
        else:
            raise HTTPException(status_code=409, detail="User not created because already exists")
    finally:
        db.close_db()
        
        
#Delegar apenas para admin qdo autenticação tiver pronta
@router.delete("/deleteuser/{id}")
async def delete_user(id: str):
   
    try:
        if (userRepository.deleteUser(id)):
            return "Deleted User"
        else: 
            raise HTTPException(status_code = 400, detail = "User not found")
    finally:
        db.close_db()
        