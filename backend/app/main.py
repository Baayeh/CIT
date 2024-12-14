from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import engine, init_db
from app.routers import auth_routes, customer_routes, ticket_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server Started")
    init_db()

    yield
    engine.dispose()


version = "v1"

app = FastAPI(version=version)

app.include_router(auth_routes.router, prefix=f"/api/{version}/auth", tags=["auth"])
app.include_router(
    customer_routes.router, prefix=f"/api/{version}/customers", tags=["customers"]
)
app.include_router(
    ticket_routes.router, prefix=f"/api/{version}/tickets", tags=["tickets"]
)
