from typing import Any, Callable

from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse


class CustomException(Exception):
    """Base class for all API-related errors."""

    pass


class InvalidToken(CustomException):
    """Raised when the provided token is invalid or expired."""

    pass


class RevokedToken(CustomException):
    """
    Raised when the provided token has been revoked.
    """

    pass


class AccessTokenRequired(CustomException):
    """
    Raised when an access token is required but a refresh token was provided.
    """

    pass


class RefreshTokenRequired(CustomException):
    """
    Raised when a refresh token is required but an access token was provided.
    """

    pass


class UserAlreadyExists(CustomException):
    """
    Raised when attempting to create a user with an email that already exists in the database.
    """

    pass


class InvalidCredentials(CustomException):
    """
    Raised when attempting to login with wrong credentials
    """

    pass


class InsufficientPermission(CustomException):
    """
    Raised when the user lacks the necessary permissions to perform an action.
    """

    pass


class TicketNotFound(CustomException):
    """Raised when the specified ticket cannot be found."""

    pass


class CustomerNotFound(CustomException):
    """Raised when the specified customer cannot be found."""

    pass


class UserNotFound(CustomerNotFound):
    """Raised when the specified user cannot be found."""

    pass


def create_exception_handler(
    status_code: int, initial_detail: Any
) -> Callable[[Request, Exception], JSONResponse]:
    async def exception_handler(request: Request, exc: CustomException):
        return JSONResponse(content=initial_detail, status_code=status_code)

    return exception_handler


def register_all_errors(app: FastAPI):
    app.add_exception_handler(
        InvalidToken,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message": "Token is invalid or expired",
                "error_code": "invalid_token",
            },
        ),
    )

    app.add_exception_handler(
        RevokedToken,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message": "Token provided has been revoked",
                "error_code": "token_revoked",
            },
        ),
    )

    app.add_exception_handler(
        AccessTokenRequired,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message": "Please provide a valid access token",
                "error_code": "access_token_required",
            },
        ),
    )

    app.add_exception_handler(
        RefreshTokenRequired,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message": "Please provide a valid refresh token",
                "error_code": "rtefresh_token_required",
            },
        ),
    )

    app.add_exception_handler(
        UserAlreadyExists,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_detail={
                "message": "User with email already exists",
                "error_code": "user_exists",
            },
        ),
    )

    app.add_exception_handler(
        InvalidCredentials,
        create_exception_handler(
            status_code=status.HTTP_400_BAD_REQUEST,
            initial_detail={
                "message": "Invalid email or password",
                "error_code": "invalid_email_or_password)",
            },
        ),
    )

    app.add_exception_handler(
        InsufficientPermission,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_detail={
                "message": "You don not have permission to perform this action",
                "error_code": "insufficient_permission",
            },
        ),
    )

    app.add_exception_handler(
        TicketNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_detail={
                "message": "Ticket not found",
                "error_code": "ticket_not_found",
            },
        ),
    )

    app.add_exception_handler(
        CustomerNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_detail={
                "message": "Customer not found",
                "error_code": "customer_not_found",
            },
        ),
    )

    app.add_exception_handler(
        UserNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_detail={
                "message": "User not found",
                "error_code": "user_not_found",
            },
        ),
    )

    @app.exception_handler(500)
    async def internal_server_error(request, exc):
        return JSONResponse(
            content={"message": "Something went wrong", "error_code": "server_error"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
