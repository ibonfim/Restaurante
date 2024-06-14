import sys
import os
from fastapi import APIRouter, Body, HTTPException
# Adicione o diretório principal ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Repository.UserRepository import UserRepository


router = APIRouter()
userRepository= UserRepository()


@router.get("/users")
async def get_users():
    conn=userRepository.get_db()
    cursor=conn.cursor()
    try:
        user=userRepository.getAllUsers(cursor)
        if user:
            return   user
        else:
            raise HTTPException(status_code=404, detail="User not found")
    finally:
        userRepository.close_db()
        
#Delegar apenas para admin qdo autenticação tiver pronta        
@router.post("/insertUser")
async def insert_menu(nome: str = Body(...), senha: str = Body(...),endereco: str= Body(...),telefone: int =Body(...),cpf: int =Body(...)):
    conn = userRepository.get_db()
    cursor = conn.cursor()
    try:
        if userRepository.insertUser(cursor, nome, senha,endereco,(telefone),(cpf)):
            return "Created User"
        else:
            raise HTTPException(status_code=409, detail="User not created because already exists")
    finally:
        userRepository.close_db()
        
        
#Delegar apenas para admin qdo autenticação tiver pronta
@router.delete("/deleteuser/{id}")
async def delete_user(id: str):
    conn=userRepository.get_db()
    cursor=conn.cursor()
    try:
        if (userRepository.deleteUser(cursor,id)):
            return "Deleted User"
        else: 
            raise HTTPException(status_code = 400, detail = "User not found")
    finally:
        userRepository.close_db()
        