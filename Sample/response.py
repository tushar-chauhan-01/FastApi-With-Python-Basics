import responseModel

def successRes(param: responseModel.successRes):
    res = {
        "Status": "Success",
        "StatusCode": param.code,
        "Message": param.msg,
        "Data": param.data
    }
    return res

def failRes(param: responseModel.failRes):
    res = {
        "Status": "Failed",
        "StatusCode": param.code,
        "Message": param.msg,
        "Data": param.data
    }
    return res