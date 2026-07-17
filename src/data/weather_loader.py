from typing import Dict
import requests
import pandas as pd

from src.utils.logging_utils import logger
from src.utils.io_utils import get_data_path


class WeatherLoader:
    def __init__(self, base_url: str, provider: str):
        self.base_url = base_url
        self.provider = provider

    def fetch_degree_days(self, region_code: str) -> pd.DataFrame:
        logger.info(f"Fetching weather/degree days for {region_code} (stub).")
        # Placeholder: integrate NOAA or other provider
        df = pd.DataFrame(columns=["date", "region", "hdd", "cdd"])
        return df

    def save_region_weather(self, region_code: str) -> pd.DataFrame:
        df = self.fetch_degree_days(region_code)
        path = get_data_path("raw", f"weather_{region_code}.csv")
        df.to_csv(path, index=False)
        logger.info(f"Saved weather data for {region_code} to {path}")
        return df
