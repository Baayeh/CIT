from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from app.db.database import SessionDep
from app.dependencies.auth_dependencies import RefreshTokenBearer
from app.schemas.auth_schema import UserCreateSchema, UserDetailSchema, UserLoginSchema
from app.services.auth_service import AuthService
from app.utils.auth_utils import create_access_token, verify_passwd

router = APIRouter()
service = AuthService()

REFRESH_TOKEN_EXPIRY = 2

TokenDep = Depends(RefreshTokenBearer())


@router.post(
    "/signup", response_model=UserDetailSchema, status_code=status.HTTP_201_CREATED
)
async def create_user_account(user_data: UserCreateSchema, session: SessionDep):
    new_user = service.create_user(user_data, session)

    return new_user


@router.post("/login")
async def login_user(login_data: UserLoginSchema, session: SessionDep):
    email = login_data.email
    password = login_data.password

    user = service.get_user_by_email(email, session)

    if user is not None:
        password_valid = verify_passwd(password, user.password_hash)

        if password_valid:
            access_token = create_access_token(
                user_data={"email": user.email, "user_id": str(user.id)}
            )

            refresh_token = create_access_token(
                user_data={"email": user.email, "user_id": str(user.id)},
                refresh=True,
                expiry=timedelta(days=REFRESH_TOKEN_EXPIRY),
            )

            return JSONResponse(
                content={
                    "message": "Login successful",
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "user": {"email": user.email, "id": str(user.id)},
                }
            )

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="Invalid email or password"
    )


@router.get("/refresh_token")
async def get_new_access_token(token_details: dict = TokenDep):
    """Get New Access Token using the refresh token"""

    expiry_timestamp = token_details["exp"]

    if datetime.fromtimestamp(expiry_timestamp) > datetime.now():
        new_access_token = create_access_token(user_data=token_details["user"])

        return JSONResponse(content={"access_token": new_access_token})
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token"
    )
