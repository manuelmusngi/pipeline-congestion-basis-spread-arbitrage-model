from typing import List, Tuple
import pandas as pd
from sklearn.linear_model import LinearRegression

from src.utils.logging_utils import logger


class CongestionModel:
    def __init__(self, feature_cols: List[str], target_col: str = "basis"):
        self.feature_cols = feature_cols
        self.target_col = target_col
        self.model = LinearRegression()

    def fit(self, df: pd.DataFrame) -> None:
        X = df[self.feature_cols].values
        y = df[self.target_col].values
        self.model.fit(X, y)
        logger.info("Fitted congestion regression model.")

    def predict(self, df: pd.DataFrame) -> pd.Series:
        X = df[self.feature_cols].values
        preds = self.model.predict(X)
        return pd.Series(preds, index=df.index, name="basis_pred")

    def fit_predict(self, train_df: pd.DataFrame,
                    test_df: pd.DataFrame) -> Tuple[pd.Series, pd.Series]:
        self.fit(train_df)
        train_pred = self.predict(train_df)
        test_pred = self.predict(test_df)
        return train_pred, test_pred
