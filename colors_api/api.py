from fastapi import FastAPI
from .routes import colors, health

app = FastAPI()

app.include_router(colors.router)
app.include_router(health.router)
