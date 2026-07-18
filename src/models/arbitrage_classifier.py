from typing import List
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from src.utils.logging_utils import logger


class ArbitrageClassifier:
    def __init__(self,
                 feature_cols: List[str],
                 threshold: float = 0.6,
                 n_estimators: int = 200,
                 max_depth: int = 6,
                 min_samples_leaf: int = 5):
        self.feature_cols = feature_cols
        self.threshold = threshold
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_leaf=min_samples_leaf,
            random_state=42,
        )

    def fit(self, df: pd.DataFrame, label_col: str) -> None:
        X = df[self.feature_cols].values
        y = df[label_col].values
        self.model.fit(X, y)
        logger.info("Fitted arbitrage classifier.")

    def predict_proba(self, df: pd.DataFrame) -> pd.Series:
        X = df[self.feature_cols].values
        proba = self.model.predict_proba(X)[:, 1]
        return pd.Series(proba, index=df.index, name="arbitrage_prob")

    def predict_signal(self, df: pd.DataFrame) -> pd.Series:
        proba = self.predict_proba(df)
        signal = (proba >= self.threshold).astype(int)
        return signal.rename("arbitrage_signal")
