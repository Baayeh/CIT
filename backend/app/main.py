from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import engine, init_db
from app.routers import customer_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server Started")
    init_db()

    yield
    engine.dispose()


version = "v1"

app = FastAPI(version=version, lifespan=lifespan)

app.include_router(customer_routes.router)
