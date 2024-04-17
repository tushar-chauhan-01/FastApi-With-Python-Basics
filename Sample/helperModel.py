from pydantic import BaseModel, validator
from typing import Optional
from fastapi import File, UploadFile, Form
from datetime import datetime,date

class Hello(BaseModel):
    firstName: Optional[str]=None
    lastName: Optional[str]=None
    age: Optional[int]=None

    
class HelloBack(BaseModel):
    firstName: str
    lastName: Optional[str]=None
    age: int

class FileUpload(BaseModel):
    fileType: str
    taskId: str
    status: int
    metadata: Optional[str]=None
    fileLat: Optional[str] = None
    fileLng: Optional[str] = None
    cameraOrientation: Optional[str] = None
    isOfflineMode: Optional[str] = None
    captureDate: Optional[datetime] = None
    zoneDetails: Optional[str] = None
    file: UploadFile
    lastUpdate: Optional[datetime] = None
    note: str
    category:Optional[str] = None

    @classmethod
    def as_form(
        cls,
        fileType: str = Form(...),
        taskId: str = Form(...),
        status: int = Form(...),
        metadata: str = Form(None),
        fileLat: str = Form(None),
        fileLng: str = Form(None),
        cameraOrientation: str = Form(None),
        file: UploadFile=File(...),
        zoneDetails: str = Form(None),
        note: str = Form(...),
        lastUpdate: str = Form(None),
        captureDate: str = Form(None),
        isOfflineMode: str = Form(None),
        category: str = Form(None),

    ):
        return cls(fileType=fileType, taskId=taskId, status=status,metadata=metadata, fileLat=fileLat, fileLng=fileLng, cameraOrientation=cameraOrientation, file=file, note=note, zoneDetails=zoneDetails, lastUpdate=lastUpdate, captureDate=captureDate, isOfflineMode=isOfflineMode,category=category)
   