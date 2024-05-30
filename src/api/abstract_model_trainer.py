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
            test_size: float) -> list[DataFrame]:
        """Split the incoming dataframe into random train and test subsets, using 
        ``test_size`` to represent the proportion of the dataset to include in the test split.

        Args:
            data (DataFrame): Dataframe.
            test_size (float): Proportion of the dataset to include in the test split.

        Returns:
            list[DataFrame]: List of ``train_dataset`` and ``test_dataset``.
        """
        pass

    @abstractmethod
    def scale_features(self, train_dataset: DataFrame, test_dataset: DataFrame) -> None:
        """Apply the fit-transform function of the provided scaler.

        Args:
            train_dataset (DataFrame): Train dataframe.
            test_dataset (DataFrame): Test dataframe.
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

    @abstractmethod
    def evaluate_model(self, test_dataset: DataFrame, model_path: str = None) -> dict | None:
        """Evaluate the model under ``model_path`` based on the provided
        ``test_dataset``. Returns a dictonary containing all the metrics.

        Args:
            test_dataset (DataFrame): Test dataframe.
            model_path (str, optional): Path to the model. Defaults to None.

        Returns:
            dict | None: Dictionary containing the metrics.
        """
        pass

    @abstractmethod
    def load_model(self, model_path: str) -> None:
        """Load the model under ``model_path`` and set it as self 
        model attribute.

        Args:
            model_path (str): Path to the model.
        """
        pass
