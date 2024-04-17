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

@router.post("/fileUpload", tags=["Uploads"])
async def fileUpload(request: Request, param: helperModel.FileUpload = Depends(helperModel.FileUpload.as_form)):
    response = "inside fileupload method"
    # response = helper.fileUpload(request, param)
    return response
