from typing import List, Dict
import requests
import pandas as pd

from src.utils.logging_utils import logger
from src.utils.io_utils import get_data_path


class EIALoader:
    def __init__(self, base_url: str, api_key: str, series_ids: Dict[str, str]):
        self.base_url = base_url
        self.api_key = api_key
        self.series_ids = series_ids

    def fetch_series(self, series_id: str) -> pd.DataFrame:
        url = f"{self.base_url}/series/?api_key={self.api_key}&series_id={series_id}"
        logger.info(f"Fetching EIA series: {series_id}")
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()["series"][0]["data"]
        df = pd.DataFrame(data, columns=["date", "value"])
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")
        return df

    def fetch_all(self) -> Dict[str, pd.DataFrame]:
        out = {}
        for name, sid in self.series_ids.items():
            out[name] = self.fetch_series(sid)
        return out

    def save_all(self) -> None:
        all_series = self.fetch_all()
        for name, df in all_series.items():
            path = get_data_path("raw", f"eia_{name}.csv")
            df.to_csv(path, index=False)
            logger.info(f"Saved EIA series {name} to {path}")
