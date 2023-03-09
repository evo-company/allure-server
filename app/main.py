from fastapi import FastAPI

from routers.report import router as report_router
from routers.result import router as result_router
from routers.ui import router as ui_router

app = FastAPI()

app.include_router(report_router, prefix="/api/report")
app.include_router(result_router, prefix="/api/result")
app.include_router(ui_router, prefix="/ui")
