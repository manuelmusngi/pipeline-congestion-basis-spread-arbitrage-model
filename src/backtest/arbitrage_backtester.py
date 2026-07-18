import pandas as pd

from src.backtest.pnl_metrics import compute_pnl
from src.utils.logging_utils import logger


class ArbitrageBacktester:
    def __init__(self,
                 capacity_mmbtu: float,
                 transaction_cost_per_mmbtu: float):
        self.capacity_mmbtu = capacity_mmbtu
        self.transaction_cost_per_mmbtu = transaction_cost_per_mmbtu

    def run(self,
            signals: pd.Series,
            realized_spread: pd.Series) -> pd.DataFrame:
        df = compute_pnl(
            signals=signals,
            realized_spread=realized_spread,
            capacity_mmbtu=self.capacity_mmbtu,
            transaction_cost_per_mmbtu=self.transaction_cost_per_mmbtu,
        )
        logger.info("Completed arbitrage backtest.")
        return df
