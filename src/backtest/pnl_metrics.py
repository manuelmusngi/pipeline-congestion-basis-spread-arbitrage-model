import pandas as pd


def compute_pnl(signals: pd.Series,
                realized_spread: pd.Series,
                capacity_mmbtu: float,
                transaction_cost_per_mmbtu: float) -> pd.DataFrame:
    df = pd.concat([signals, realized_spread], axis=1)
    df.columns = ["signal", "spread"]

    df["position_mmbtu"] = df["signal"] * capacity_mmbtu
    df["gross_pnl"] = df["position_mmbtu"] * df["spread"]
    df["transaction_cost"] = abs(df["position_mmbtu"]) * transaction_cost_per_mmbtu
    df["net_pnl"] = df["gross_pnl"] - df["transaction_cost"]

    return df
