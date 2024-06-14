
import os
import sys
from fastapi import FastAPI
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Models import tables
from Controller import MenuControler, UsersControler  # Import the router modules



app = FastAPI()

# Include the routers
app.include_router(MenuControler.router)
app.include_router(UsersControler.router)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8500)

 