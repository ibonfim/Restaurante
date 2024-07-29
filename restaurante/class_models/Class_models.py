from pydantic import BaseModel, Field, constr, condecimal, field_validator
from typing import Literal, Optional
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class User(BaseModel):
    CPF: int  
    endereco: str
    telefone: int
    nome: str
    senha: str
    usertype: Literal['ADMIN', 'USER'] = 'USER'

class Pedido(BaseModel):
    descricao: str
    id_user: int
    id: Optional[int] = None

class Cardapio(BaseModel):
    nome: str
    id: Optional[int] = None
    valor: float
    
    @field_validator('valor')
    def validate_valor(cls, v):
        if round(v, 2) != v:
            raise ValueError('O valor deve ter no máximo duas casas decimais')
        return v
