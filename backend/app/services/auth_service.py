from fastapi import HTTPException, status
from sqlmodel import Session, select

from app.models.auth_model import User
from app.schemas.auth_schema import UserCreateSchema
from app.utils.auth_utils import generate_passwd_hash


class AuthService:
    def get_user_by_email(self, email: str, session: Session):
        """Get user from DB using the email"""
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User was not found",
            )

        return user

    def user_exists(self, email: str, session: Session):
        """Check if user already exists"""

        statement = select(User).where(User.email == email)
        return session.exec(statement).first() is not None

    def create_user(self, user_data: UserCreateSchema, session: Session):
        user_exists = self.user_exists(user_data.email, session)

        if user_exists:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User with email already exists",
            )

        user_data_dict = user_data.model_dump()

        new_user = User(**user_data_dict)

        new_user.password_hash = generate_passwd_hash(user_data_dict["password"])

        session.add(new_user)
        session.commit()

        return new_user
