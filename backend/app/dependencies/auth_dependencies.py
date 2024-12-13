from app.utils.auth_utils import decode_token
from fastapi import Request, status
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error=True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        """
        Validate the token and return its decoded data.
        """

        credentials = await super().__call__(request)

        token = credentials.credentials

        # Decode and validate the token
        token_data = self.is_token_valid(token)

        self.verify_token_data(token_data)

        return token_data

    def is_token_valid(self, token: str) -> dict:
        """
        Decode the token safely and return its data if valid.
        Raise appropriate HTTP exceptions for known issues.
        """

        token_data = decode_token(token)

        if token_data is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid or expired token"
            )
        return token_data

    def verify_token_data(self, token_data):
        """
        Verify the structure or claims of the token.
        This method must be implemented in subclasses for custom logic.
        """
        raise NotImplementedError("Please overide this method in child class")


class AccessTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please provide an access token",
            )


class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data and not token_data["refresh"]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Please provide a refresh token",
            )
