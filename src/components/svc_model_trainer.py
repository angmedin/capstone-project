from joblib import load
from pandas import DataFrame
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC

from api.abstract_model_trainer import AbstractModelTrainer
from entity.bean import BeanProperties as bp


class SVCModelTrainer(AbstractModelTrainer):
    """Specific implementation of the ``AbstractModelTrainer`` base class.
    Provides an implementation of the C-Support Vector Classification. 

    Args:
        AbstractModelTrainer (_type_): Abstract base class.
    """

    def __init__(self, max_iter: int = 1000, random_state: int = 42) -> None:
        self.model = SVC(max_iter=max_iter, random_state=random_state)
        self.encoder = LabelEncoder()
        self.scaler = StandardScaler()

    def drop_columns(self, data: DataFrame) -> DataFrame:
        columns_to_drop = [
            bp.area,
            bp.perimeter,
            bp.compactness,
            bp.shape_factor_3
        ]
        return data.drop(columns=columns_to_drop)

    def encode_labels(self, data: DataFrame) -> None:
        data[bp.clazz] = self.encoder.fit_transform(data[bp.clazz])

    def split_train_test_data(
            self,
            data: DataFrame,
            test_size: float,
            random_state: int) -> list[DataFrame]:
        return train_test_split(
            data,
            test_size=test_size,
            random_state=random_state,
            shuffle=True)

    def scale_features(self, train_dataset: DataFrame) -> None:
        columns: list[str] = train_dataset.columns.drop(bp.clazz).to_list()

        train_dataset[columns] = DataFrame(
            self.scaler.fit_transform(train_dataset[columns]),
            index=train_dataset.index)

    def train_model(self, train_data: DataFrame) -> SVC:
        X = train_data.drop([bp.clazz], axis=1)
        y = train_data[bp.clazz]

        return self.model.fit(X, y)

    def evaluate_model(self, test_dataset: DataFrame, model_path: str = None) -> dict | None:
        if model_path is not None:
            self.load_model(model_path=model_path)

        y_test = test_dataset.loc[:, bp.clazz]
        X_test = test_dataset.drop(bp.clazz, axis=1)

        if self.model.fit_status_ != 0:
            return None

        y_pred = self.model.predict(X_test)
        print(set(y_test) - set(y_pred))
        return classification_report(
            y_true=y_test, y_pred=y_pred, output_dict=True)

    def load_model(self, model_path: str) -> None:
        self.model = load(model_path)
