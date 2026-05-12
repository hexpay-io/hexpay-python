from enum import Enum


class PaymentStatus(str, Enum):
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    CREATED = "created"
    EXPIRED = "expired"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
