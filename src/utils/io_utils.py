import os
from pathlib import Path
from typing import Union

import pandas as pd
import yaml


BASE_DIR = Path(__file__).resolve().parents[2]


def get_data_path(*parts: str) -> Path:
    return BASE_DIR / "data" / Path(*parts)


def load_yaml_config(path: Union[str, Path]) -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)


def save_dataframe(df: pd.DataFrame, path: Union[str, Path]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def load_dataframe(path: Union[str, Path]) -> pd.DataFrame:
    return pd.read_csv(path)
