import pandas as pd
from data_reporter import DataReporter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from entity.bean import BeanProperties as bp


class ModelTrainer():
    def __init__(self):
        self.data_reporter = DataReporter()
        self.svc = SVC()

    def train_model(self):
        data = self.data_reporter.get_filtered_bean_data()

        if data is None:
            return

        X_train, X_test, y_train, y_test = self.split_data(data=data)

        self.feature_scale(X_train, X_test)
        self.remove_correlated_features(X_train, X_test)

        self.svc.fit(X_train, y_train)

    def split_data(self, data: pd.DataFrame) -> list:
        features = data.drop(columns=[bp.clazz]).columns
        X = data[features]
        y = data[bp.clazz]

        return train_test_split(X, y, test_size=0.2, train_size=0.8, random_state=None, shuffle=True)

    def feature_scale(self, X_train: pd.DataFrame, X_test: pd.DataFrame) -> None:
        columns: list[str] = X_train.columns.to_list()

        standard_scaler = StandardScaler()
        X_train[columns] = pd.DataFrame(standard_scaler.fit_transform(
            X_train[columns]), index=X_train.index)
        X_test[columns] = pd.DataFrame(
            standard_scaler.fit_transform(X_test[columns]), index=X_test.index)

    def remove_correlated_features(self, X_train: pd.DataFrame, X_test: pd.DataFrame) -> None:
        dropped_columns = [bp.area, bp.perimeter,
                           bp.compactness, bp.shape_factor_3]
        X_train = X_train.drop(columns=dropped_columns)
        X_test = X_test.drop(columns=dropped_columns)
