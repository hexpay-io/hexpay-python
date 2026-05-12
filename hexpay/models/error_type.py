from enum import Enum


class ErrorType(str, Enum):
    API_ERROR = "api_error"
    AUTHENTICATION_ERROR = "authentication_error"
    INVALID_REQUEST_ERROR = "invalid_request_error"
    NOT_FOUND_ERROR = "not_found_error"
    RATE_LIMIT_ERROR = "rate_limit_error"

    def __str__(self) -> str:
        return str(self.value)
