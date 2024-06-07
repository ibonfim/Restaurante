import sys
import os
from fastapi import APIRouter, HTTPException
# Adicione o diretório principal ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Models.tables import *
from Sql.Sql import *


router = APIRouter()



@router.get("/users")
async def get_users():
    conn=get_db()
    cursor=conn.cursor()
    try:
        user=getAllUsers(cursor)
        if user:
            return   user
        else:
            raise HTTPException(status_code=404, detail="User not found")
    finally:
        close_db(conn)