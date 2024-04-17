from pandas import DataFrame
from common.logger import Logger


class DryBeanEntity():
    def __init__(self) -> None:
        self.eccentricity
        self.convex_area
        self.solidity
        self.roundness
        self.shape_factor_1
        self.shape_factor_4


class DataProcessor():
    def __init__(self) -> None:
        self.logger = Logger()

    def filter(self, data: DataFrame) -> DataFrame:
        data = data[data['Eccentricity'] >= 0.3]
        data = data[data['ConvexArea'] <= 250000]
        data = data[data['Solidity'] >= 0.94]
        data = data[data['roundness'] >= 0.51]
        data = data[data['ShapeFactor1'] <= 0.0104]
        data = data[data['ShapeFactor4'] >= 0.954]

        return data
