import argparse
from pathlib import Path

from src.utils.io_utils import load_yaml_config, load_dataframe, save_dataframe
from src.utils.logging_utils import logger
from src.features.basis_features import compute_basis, add_basis_features
from src.models.congestion_regression import CongestionModel
from src.models.arbitrage_classifier import ArbitrageClassifier
from src.backtest.arbitrage_backtester import ArbitrageBacktester


def parse_args():
    parser = argparse.ArgumentParser(
        description="Pipeline Congestion & Basis Spread Arbitrage Pipeline"
    )
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to model_params.yaml",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    cfg = load_yaml_config(args.config)

    # --- Load example data (you’ll wire real sources) ---
    hh = load_dataframe("data/processed/hh_prices.csv")
    reg = load_dataframe("data/processed/chcg_prices.csv")

    basis_df = compute_basis(hh, reg)
    basis_df = add_basis_features(
        basis_df,
        lookback_days=cfg["basis_features"]["lookback_days"],
        vol_window=cfg["basis_features"]["volatility_window"],
        zscore_window=cfg["basis_features"]["zscore_window"],
    )

    # Dummy congestion features & labels for illustration
    basis_df["utilization_ratio"] = 0.9
    basis_df["has_critical_notice"] = 0
    basis_df["arbitrage_label"] = (basis_df["basis_zscore"].abs() > 2).astype(int)

    feature_cols = ["basis_roll_mean", "basis_roll_std", "basis_zscore",
                    "utilization_ratio", "has_critical_notice"]

    # --- Congestion regression ---
    cong_model = CongestionModel(feature_cols=feature_cols, target_col="basis")
    train_df = basis_df.iloc[:-100]
    test_df = basis_df.iloc[-100:]
    train_pred, test_pred = cong_model.fit_predict(train_df, test_df)

    # --- Arbitrage classifier ---
    clf = ArbitrageClassifier(
        feature_cols=feature_cols,
        threshold=cfg["arbitrage_classifier"]["threshold"],
        n_estimators=cfg["arbitrage_classifier"]["n_estimators"],
        max_depth=cfg["arbitrage_classifier"]["max_depth"],
        min_samples_leaf=cfg["arbitrage_classifier"]["min_samples_leaf"],
    )
    clf.fit(train_df, label_col="arbitrage_label")
    signals = clf.predict_signal(test_df)

    # --- Backtest ---
    backtester = ArbitrageBacktester(
        capacity_mmbtu=cfg["backtest"]["capacity_limit_mmbtu"],
        transaction_cost_per_mmbtu=cfg["backtest"]["transaction_cost_per_mmbtu"],
    )
    backtest_df = backtester.run(
        signals=signals,
        realized_spread=test_df["basis"],
    )

    save_dataframe(backtest_df, "data/processed/backtest_results.csv")
    logger.info("Pipeline run complete. Backtest results saved.")


if __name__ == "__main__":
    main()
