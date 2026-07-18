import pandas as pd

from src.utils.logging_utils import logger


def build_imbalance_metrics(weather_df: pd.DataFrame,
                            storage_df: pd.DataFrame,
                            region_code: str) -> pd.DataFrame:
    w = weather_df.copy()
    s = storage_df.copy()

    s["storage_dev_5yr"] = s["storage"] - s["storage_5yr_avg"]

    df = pd.merge(w, s, on="date", how="left")
    df["region"] = region_code
    logger.info("Built regional imbalance metrics.")
    return df
