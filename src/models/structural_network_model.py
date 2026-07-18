from dataclasses import dataclass
from typing import Dict

import pandas as pd

from src.utils.logging_utils import logger


@dataclass
class StructuralNetworkParams:
    storage_elasticity: float
    transport_elasticity: float
    base_spread: float


class StructuralNetworkModel:
    """
    Stylized structural model inspired by Oliver-Mason-Finnoff:
    basis ≈ base_spread + λ * congestion - μ * storage
    """

    def __init__(self, params: StructuralNetworkParams):
        self.params = params

    def compute_structural_basis(self,
                                 congestion_index: pd.Series,
                                 storage_index: pd.Series) -> pd.Series:
        λ = self.params.transport_elasticity
        μ = self.params.storage_elasticity
        base = self.params.base_spread

        basis = base + λ * congestion_index - μ * storage_index
        logger.info("Computed structural basis from congestion and storage indices.")
        return basis.rename("basis_structural")
