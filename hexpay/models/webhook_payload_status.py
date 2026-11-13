from enum import Enum


class WebhookPayloadStatus(str, Enum):
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
