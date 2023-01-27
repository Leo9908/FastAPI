from fastapi import FastAPI
from src.routes import auth, users, products

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
