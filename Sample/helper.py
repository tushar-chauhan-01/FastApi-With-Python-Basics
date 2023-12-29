import traceback
import helperModel, response, responseModel
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv
load_dotenv(os.path.join(BASE_DIR,"Sample\.env"))


def hello(param : helperModel.Hello, request):
    try:
        
        hello_greeting=f"Hello, I am {os.getenv('FIRSTNAME')} {os.getenv('LASTNAME')}. I am {os.getenv('AGE')} years old. I am from {os.getenv('COUNTRY')}"
        return response.successRes( responseModel.successRes( code="200", msg=hello_greeting, data=[] ) )
    
    except Exception as e:
        print(traceback.print_exc())
        return response.failRes( responseModel.failRes( code="400", msg=str(e), data=[] ))
    
    
async def helloBack(param : helperModel.HelloBack, request):
    try:
        
        bye_greeting=f"Hello, I am {param.firstName} {param.lastName}. I am {param.age} years old. I am from {os.getenv('COUNTRY')}"
        return response.successRes( responseModel.successRes( code="200", msg=bye_greeting, data=[] ) )
    
    except Exception as e:
        print(traceback.print_exc())
        return response.failRes( responseModel.failRes( code="400", msg=str(e), data=[] ))
    
