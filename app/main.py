from fastapi import FastAPI
from app.routers.auth import router
from app.routers.tasks import tasks_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/auth", tags=["Authentication"])
app.include_router(tasks_router, prefix="/api", tags=["Tasks"])
