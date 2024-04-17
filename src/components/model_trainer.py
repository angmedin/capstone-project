class ModelTrainer():
    def split_data():
        features = data.drop(columns=['Class']).columns
        X = data[features]
        y = data['Class']
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, train_size=0.8, random_state=None, shuffle=True)

    def feature_scale():
        columns: list[str] = X_train.columns.to_list()

        standard_scaler = StandardScaler()
        X_train[columns] = pd.DataFrame(standard_scaler.fit_transform(X_train[columns]), index=X_train.index)
        X_test[columns] = pd.DataFrame(standard_scaler.fit_transform(X_test[columns]), index=X_test.index)

    def fit():
        model.fit(X_train, y_train)