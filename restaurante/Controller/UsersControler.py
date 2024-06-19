import sys
import os
from fastapi import APIRouter, Body, HTTPException
# Adicione o diretório principal ao sys.path
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Repository.UserRepository import UserRepository
from db.db import bdata

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
async def insert_menu(nome: str = Body(...), cpf: int = Body(...),endereco: str= Body(...),telefone: int =Body(...),senha: str =Body(...),usertype: str=Body(...)):
    
    try:
        if userRepository.insertUser(nome,cpf,endereco,telefone,senha,usertype):
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
        