from typing import Dict
import pandas as pd
import numpy as np

from src.utils.logging_utils import logger


def compute_basis(hub_df: pd.DataFrame,
                  regional_df: pd.DataFrame,
                  date_col: str = "date",
                  price_col: str = "value") -> pd.DataFrame:
    merged = pd.merge(hub_df, regional_df,
                      on=date_col,
                      suffixes=("_hub", "_reg"))
    merged["basis"] = merged[f"{price_col}_reg"] - merged[f"{price_col}_hub"]
    return merged[[date_col, "basis"]]


def add_basis_features(basis_df: pd.DataFrame,
                       lookback_days: int,
                       vol_window: int,
                       zscore_window: int) -> pd.DataFrame:
    df = basis_df.copy()
    df = df.sort_values("date")
    df["basis_roll_mean"] = df["basis"].rolling(lookback_days).mean()
    df["basis_roll_std"] = df["basis"].rolling(vol_window).std()
    df["basis_zscore"] = (
        df["basis"] - df["basis"].rolling(zscore_window).mean()
    ) / df["basis"].rolling(zscore_window).std()
    logger.info("Computed basis features.")
    return df
