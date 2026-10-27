from fastapi import FastAPI
from app.routers.menu import router as menu_router

app = FastAPI(
    title="Lab 5 – API thực đơn căng tin trường",
    description="Thiết kế CRUD, phân lớp schema/repository/router và kiểm thử Postman",
    version="1.0.0",
)
app.include_router(menu_router)


@app.get("/health", tags=["System"])
def health():
    return {"status": "ok"}
