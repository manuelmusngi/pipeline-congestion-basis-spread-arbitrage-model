import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def plot_basis_series(df: pd.DataFrame,
                      date_col: str,
                      basis_col: str,
                      title: str = "Basis Spread") -> None:
    plt.figure(figsize=(12, 5))
    sns.lineplot(data=df, x=date_col, y=basis_col)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Basis ($/MMBtu)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
