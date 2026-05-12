from enum import Enum


class CoinResponseSymbol(str, Enum):
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
