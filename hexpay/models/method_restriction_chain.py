from enum import Enum


class MethodRestrictionChain(str, Enum):
    TON = "TON"

    def __str__(self) -> str:
        return str(self.value)
