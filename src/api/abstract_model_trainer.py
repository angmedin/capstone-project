from abc import ABC, abstractmethod

from pandas import DataFrame


class AbstractModelTrainer(ABC):

    @abstractmethod
    def drop_columns(self, data: DataFrame) -> DataFrame:
        """Drop specified labels from columns.
        Dropped columns are unused features, accordingly to the performed EDA.

        Args:
            data (DataFrame): Raw dataframe.

        Returns:
            DataFrame: Dataframe after dropped columns.
        """
        pass

    @abstractmethod
    def encode_labels(self, data: DataFrame) -> None:
        """Encode target labels with value between 0 and n_classes-1 using 
        specific encoder.

        Args:
            data (DataFrame): Dataframe.
        """
        pass

    @abstractmethod
    def split_train_test_data(
            self,
            data: DataFrame,
            test_size: float,
            random_state: int) -> list[DataFrame]:
        """Split the incoming dataframe into random train and test subsets, using 
        ``test_size`` to represent the proportion of the dataset to include in the test split.

        Args:
            data (DataFrame): Dataframe.
            test_size (float): Proportion of the dataset to include in the test split.
            random_state (int): Controls the shuffling applied to the data before applying the split.

        Returns:
            list[DataFrame]: List of ``train_dataset`` and ``test_dataset``.
        """
        pass

    @abstractmethod
    def scale_features(self, train_dataset: DataFrame) -> None:
        """Apply the fit-transform function of the provided scaler.

        Args:
            train_dataset (DataFrame): Dataframe.
        """
        pass

    @abstractmethod
    def train_model(self, train_data: DataFrame) -> object:
        """Train the provided model in the implemented class. 
        Returns an object of the model class.

        Args:
            train_data (DataFrame): Train dataframe.

        Returns:
            object: Model.
        """
        pass