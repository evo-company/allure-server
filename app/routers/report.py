from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ReportResponseModel(BaseModel):
    uuid: str
    path: str
    url: str


class ExecutorInfoModel(BaseModel):
    name: str
    type: str
    url: str
    buildOrder: int
    buildName: str
    buildUrl: str
    reportName: str
    reportUrl: str


class ReportSpecModel(BaseModel):
    path: List[str]
    executorInfo: ExecutorInfoModel
    results: List[str]
    deleteResults: bool


class ReportRequestModel(BaseModel):
    reportSpec: ReportSpecModel


@router.get("", response_model=List[ReportResponseModel], tags=["report"])
def get_report(path: str) -> List[ReportResponseModel]:
    return [
        ReportResponseModel(
            uuid="3fa85f64-5717-4562-b3fc-2c963f66afa6",
            path="string",
            url="string",
        )
    ]


@router.post("", response_model=ReportResponseModel, tags=["report"])
def generate_report(report_request: ReportRequestModel) -> ReportResponseModel:
    return ReportResponseModel(
        uuid="3fa85f64-5717-4562-b3fc-2c963f66afa6", path="string", url="string"
    )
