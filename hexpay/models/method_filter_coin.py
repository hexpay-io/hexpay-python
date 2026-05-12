from enum import Enum


class MethodFilterCoin(str, Enum):
    BLUM = "BLUM"
    BUILD = "BUILD"
    DOGS = "DOGS"
    DUST = "DUST"
    DYOR = "DYOR"
    NOT = "NOT"
    STON = "STON"
    TON = "TON"
    USDT = "USDT"
    XAUT0 = "XAUt0"

    def __str__(self) -> str:
        return str(self.value)
