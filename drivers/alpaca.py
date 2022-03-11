import pdb;
pdb.set_trace()
from abc import ABC
from datetime import datetime
from typing import Any, Dict, List
# from jesse.services import env
from jesse.modes.import_candles_mode.drivers.interface import CandleExchange
from DataManager.datamgr import data_manager



class AlpacaDriver(CandleExchange, ABC):
    def __init__(self):
        super().__init__(name='Alpaca', 
                         count=10_000, 
                         rate_limit_per_second=500, 
                         backup_exchange_class=None,
                         )
        self.this_manager = data_manager.DataManager(
                                                limit=None,
                                                update_before=True,
                                                exchangeName='NYSE',
                                                isDelisted=False,
                                                )
        

    def fetch(self, symbol: str, start_timestamp: int) -> List[Dict[str, Any]]:
        end_timestamp = start_timestamp + (self.count - 1) * 60000
        
        start_timestamp_str = datetime.utcfromtimestamp(start_timestamp/1000).strftime('%Y-%m-%d')
        end_timestamp_str = datetime.utcfromtimestamp(end_timestamp/1000).strftime('%Y-%m-%d')
        dict_of_dfs = self.this_manager.get_stock_data(
                            start_timestamp_str,
                            end_timestamp_str,
                            api="Alpaca"
                            )
        import pdb;
        pdb.set_trace()


    def get_starting_time(self, symbol: str) -> int:
        return 1

