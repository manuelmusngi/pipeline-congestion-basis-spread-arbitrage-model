#### Pipeline-Congestion-Basis-Spread-Arbitrage-Model

Pipeline Congestion & Basis Spread Arbitrage Model
Identifying physical‑constraint‑driven arbitrage windows in U.S. Natural Gas markets

📌 1. Overview
This project is a repository that implements a structural + statistical modeling framework to detect pipeline congestion, regional imbalances, and basis spread dislocations in U.S. natural gas markets.

The model identifies arbitrage windows where:
- Pipeline constraints create persistent price wedges
- Storage availability mitigates or amplifies spreads
- Regional imbalances (weather, outages, flows) distort locational pricing
- Capacity scarcity rents emerge in secondary markets

This framework is grounded in the structural economic model of pipeline congestion developed by Oliver, Mason & Finnoff (2014), which shows that:
- Congestion increases the scarcity value of transmission capacity
- This drives a wedge between spot prices across hubs
- Storage availability reduces the congestion‑induced spread

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

#### Research Reference

- [Pipeline Congestion and Basis Differentials](https://www.researchgate.net/publication/266908988_Pipeline_Congestion_and_Basis_Differentials)

#### License
This project is licensed under the [MIT License](LICENSE).
