import sys
import os
from fastapi import APIRouter,HTTPException
# Adicione o diretório principal ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Models.tables import *
from Sql.Sql import *



router = APIRouter()

 
# Rota para o método GET
@router.get("/menu")
async def get_cardapio():
    conn=get_db()
    cursor=conn.cursor()
    try:
        cardapio=getCardapio(cursor)
        if cardapio:
            return   cardapio
        else:
            raise HTTPException(status_code=404, detail="Menu not found")
    finally:
        close_db(conn)
        
        

 
 