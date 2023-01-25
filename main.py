from fastapi import FastAPI
from src.routes import users, products

app = FastAPI()

app.include_router(users.router)
app.include_router(products.router)
