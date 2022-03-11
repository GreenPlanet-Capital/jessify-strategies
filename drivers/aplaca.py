from abc import ABC

from jesse.modes.import_candles_mode import CandleExchange

class AlpacaDriver(CandleExchange, ABC):
    def __init__(self, name: str, count: int, rate_limit_per_second: float, backup_exchange_class):
        super().__init__(name, count, rate_limit_per_second, backup_exchange_class)

    def fetch(self, symbol: str, start_timestamp: int) -> list:
        pass

    def get_starting_time(self, symbol: str) -> int:
        pass

