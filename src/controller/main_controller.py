
from fastapi import APIRouter, Depends, Request
from fastapi.security import HTTPBearer
from datetime import datetime

main_controller = APIRouter(prefix="/main", tags=["Main controller test"])
security = HTTPBearer()

@main_controller.get(
    "/",
    description="",
    responses={}
)
def index():
    return { 'message': 'Server alive!', 'time': datetime.now() }