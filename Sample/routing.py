from fastapi import APIRouter, File, UploadFile, Form, Depends , BackgroundTasks
from starlette.requests import Request
import helperModel, helper
from starlette.requests import Request

router = APIRouter()

@router.get("/hello",tags=["Greeting"])
def hello(param: helperModel.Hello, request: Request):
    response = helper.hello(param, request)
    return response

@router.post("/helloBack",tags=["Greeting"])
async def helloBack(param: helperModel.HelloBack, request: Request):
    response = await helper.helloBack(param, request)
    return response