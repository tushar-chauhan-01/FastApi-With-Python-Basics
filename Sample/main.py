from fastapi import FastAPI
from fastapi import APIRouter
import routing

router = APIRouter()
app = FastAPI()

app.include_router(routing.router)
