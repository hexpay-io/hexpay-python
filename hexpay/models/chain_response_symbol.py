from enum import Enum


class ChainResponseSymbol(str, Enum):
    TON = "TON"

    def __str__(self) -> str:
        return str(self.value)
