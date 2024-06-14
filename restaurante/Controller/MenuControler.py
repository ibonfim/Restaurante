import sys
import os
from fastapi import Body

from fastapi import APIRouter,HTTPException
# Adicione o diretório principal ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Repository.MenuRepository import MenuRepository
menuRepository = MenuRepository()

router = APIRouter()

 
# Rota para o método GET
@router.get("/menu")
async def get_cardapio():
    conn=menuRepository.get_db()
    cursor=conn.cursor()
    try:
        cardapio=menuRepository.getCardapio(cursor)
        if cardapio:
            return   cardapio
        else:
            raise HTTPException(status_code=404, detail="Menu not found")
    finally:
        menuRepository.close_db()
        

#Delegar apenas para admin qdo autenticação tiver pronta       
@router.post("/insertmenu")
async def insert_menu(nome: str = Body(...), valor: float = Body(...)):
    conn = menuRepository.get_db()
    cursor = conn.cursor()
    print(nome, valor)
    try:
        if menuRepository.insertItemMenu(cursor, nome, valor):
            return "ok"
        else:
            raise HTTPException(status_code=500, detail="Not Inserted Item")
    finally:
        menuRepository.close_db()
        
        
#Delegar apenas para admin qdo autenticação tiver pronta       
@router.delete("/deleteitemmenu/{id}")
async def delete_item(id: str):
    conn=menuRepository.get_db()
    cursor=conn.cursor()
    try:
        if (menuRepository.deleteItemMenu(cursor,id)):
            return "Deleted Item"
        else: 
            raise HTTPException(status_code = 400, detail = "Item not found")
    finally:
        menuRepository.close_db()
        
    


        

 
 