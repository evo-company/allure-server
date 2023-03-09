from typing import List
from datetime import datetime

from fastapi import APIRouter, File
from pydantic import BaseModel

router = APIRouter()


class ResultResponseModel(BaseModel):
    uuid: str
    size: int
    created: datetime


class ResultFileResponseModel(BaseModel):
    fileName: str
    uuid: str


@router.get("", response_model=List[ResultResponseModel], tags=["result"])
def get_all_result():
    return [ResultResponseModel(uuid="uuid", size=0, created=datetime.now())]


@router.get("/{uuid}", response_model=ResultResponseModel, tags=["result"])
def get_result(uuid: str):
    return ResultResponseModel(uuid=uuid, size=0, created=datetime.now())


@router.post("", response_model=ResultResponseModel, tags=["result"])
def post_result(file: bytes = File()):
    return ResultFileResponseModel(
        fileName="fileName",
        uuid="uuid",
    )
