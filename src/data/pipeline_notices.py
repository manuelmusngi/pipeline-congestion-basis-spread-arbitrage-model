from typing import List, Dict
import requests
import pandas as pd

from src.utils.logging_utils import logger
from src.utils.io_utils import get_data_path


class PipelineNoticesLoader:
    def __init__(self, ferc_base_url: str, ebb_providers: List[Dict]):
        self.ferc_base_url = ferc_base_url
        self.ebb_providers = ebb_providers

    def fetch_ferc_notices(self) -> pd.DataFrame:
        # Placeholder: structure for FERC notices scraping/parsing
        logger.info("Fetching FERC pipeline notices (stub).")
        df = pd.DataFrame(columns=["date", "pipeline", "type", "description"])
        return df

    def fetch_ebb_notices(self) -> pd.DataFrame:
        rows = []
        for provider in self.ebb_providers:
            logger.info(f"Fetching EBB notices for {provider['name']} (stub).")
            # Placeholder: implement HTML scraping / API calls
            rows.append({
                "date": None,
                "pipeline": provider["name"],
                "type": "CRITICAL_NOTICE",
                "description": "Stub notice"
            })
        return pd.DataFrame(rows)

    def build_notices_dataset(self) -> pd.DataFrame:
        ferc_df = self.fetch_ferc_notices()
        ebb_df = self.fetch_ebb_notices()
        df = pd.concat([ferc_df, ebb_df], ignore_index=True)
        path = get_data_path("raw", "pipeline_notices.csv")
        df.to_csv(path, index=False)
        logger.info(f"Saved pipeline notices to {path}")
        return df
