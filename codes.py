
# Modelo de dados usando Pydantic
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

# Simulação de banco de dados
db = {
    "alice": {"username": "alice", "email": "alice@example.com"},
    "bob": {"username": "bob", "email": "bob@example.com"}
}


 
# Rota para o método GET
@app.get("/users/{username}", response_model=User)
async def get_user(username: str):
    
    user = db.get(username)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
    

# Rota para o método POST
@app.post("/users", response_model=User, status_code=201)
async def create_user(user: User):
    if user.username in db:
        raise HTTPException(status_code=400, detail="Username already exists")
    db[user.username] = user.model_dump()
    return user