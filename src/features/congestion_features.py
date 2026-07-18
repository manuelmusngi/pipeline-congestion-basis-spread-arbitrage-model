import pandas as pd

from src.utils.logging_utils import logger


def build_congestion_features(capacity_df: pd.DataFrame,
                              notices_df: pd.DataFrame) -> pd.DataFrame:
    df = capacity_df.copy()
    df["utilization_ratio"] = df["scheduled"] / df["capacity"]
    df["is_constrained"] = df["utilization_ratio"] > 0.95

    notices_flag = (
        notices_df
        .assign(flag=1)
        .groupby(["date", "pipeline"])["flag"]
        .max()
        .reset_index()
        .rename(columns={"flag": "has_critical_notice"})
    )

    df = df.merge(
        notices_flag,
        on=["date", "pipeline"],
        how="left"
    )
    df["has_critical_notice"] = df["has_critical_notice"].fillna(0)
    logger.info("Built congestion features.")
    return df
