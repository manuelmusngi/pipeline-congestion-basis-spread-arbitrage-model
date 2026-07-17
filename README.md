#### Pipeline-Congestion-Basis-Spread-Arbitrage-Model
*Identifying Physical‑Constraint‑Driven Arbitrage Windows in U.S. Natural Gas Markets*

📁 Project Structure

pipeline-congestion-basis-model/\
│\
├── README.md\
├── pyproject.toml\
├── requirements.txt\
├── config/\
│   ├── data_sources.yaml\
│   ├── model_params.yaml\
│   └── regions.yaml\
│\
├── data/\
│   ├── raw/\
│   ├── processed/\
│   └── external/\
│\
├── notebooks/\
│   ├── 01_data_exploration.ipynb\
│   ├── 02_basis_spread_features.ipynb\
│   ├── 03_congestion_modeling.ipynb\
│   └── 04_backtest_arbitrage_windows.ipynb\
│\
├── src/\
│   ├── __init__.py\
│   ├── data/\
│   │   ├── eia_loader.py\
│   │   ├── pipeline_notices.py\
│   │   ├── capacity_scraper.py\
│   │   └── weather_loader.py\
│   │\
│   ├── features/\
│   │   ├── basis_features.py\
│   │   ├── congestion_features.py\
│   │   └── imbalance_metrics.py\
│   │\
│   ├── models/\
│   │   ├── congestion_regression.py\
│   │   ├── structural_network_model.py\
│   │   └── arbitrage_classifier.py\
│   │\
│   ├── backtest/\
│   │   ├── arbitrage_backtester.py\
│   │   └── pnl_metrics.py\
│   │\
│   └── utils/\
│       ├── logging_utils.py\
│       ├── io_utils.py\
│       └── plotting.py\
│\
└── main.py
