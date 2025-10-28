from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.all_routers import all_routers


app = FastAPI()

for router in all_routers:
    app.include_router(router)

origins = [
    "http://localhost:5174",
    "http://127.0.0.1:5174"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)