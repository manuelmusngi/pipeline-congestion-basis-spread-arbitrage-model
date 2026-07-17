from typing import List, Dict
import pandas as pd

from src.utils.logging_utils import logger
from src.utils.io_utils import get_data_path


class CapacityScraper:
    def __init__(self, ebb_providers: List[Dict]):
        self.ebb_providers = ebb_providers

    def fetch_capacity(self) -> pd.DataFrame:
        logger.info("Fetching pipeline capacity and utilization (stub).")
        df = pd.DataFrame(columns=[
            "date", "pipeline", "segment", "scheduled", "capacity", "utilization"
        ])
        return df

    def save_capacity(self) -> pd.DataFrame:
        df = self.fetch_capacity()
        path = get_data_path("raw", "pipeline_capacity.csv")
        df.to_csv(path, index=False)
        logger.info(f"Saved pipeline capacity to {path}")
        return df
