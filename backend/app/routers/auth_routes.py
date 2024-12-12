from fastapi import APIRouter, status

from app.db.database import SessionDep
from app.schemas.auth_schema import UserCreateSchema, UserDetailSchema
from app.services.auth_service import AuthService

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])
service = AuthService()


@router.post(
    "/signup", response_model=UserDetailSchema, status_code=status.HTTP_201_CREATED
)
async def create_user_account(user_data: UserCreateSchema, session: SessionDep):
    new_user = service.create_user(user_data, session)

    return new_user
