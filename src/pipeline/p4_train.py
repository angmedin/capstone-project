import argparse
import logging

import joblib
import pandas as pd
import yaml
from dvclive import Live
from sklearn.svm import SVC

from entity.bean import BeanProperties as bp
from utils.dir_utils import DirUtils


def train_model(config_path: str) -> None:
    """Train model.
    Args:
        config_path {str}: Path to yaml configuration file.
    """

    logging.info("Stage 4: train.")

    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)

    logging.info('Load train dataset.')
    train_df = pd.read_csv(config['data_split']['trainset_path'])

    # Split the data into features (X) and target variable (y)
    X = train_df.drop([bp.clazz], axis=1)
    y = train_df[bp.clazz]

    # Create model
    logging.info('Train model.')
    model = SVC(max_iter=1000, random_state=42)

    # Fit the model to the training data
    model.fit(X, y)

    # Save the model
    models_path = config['train']['model_path']

    try:
        DirUtils.exists_else_create_dir(models_path)
        joblib.dump(model, models_path)
        logging.info(f"Model saved successfully in {models_path}.")
    except Exception as e:
        logging.error(e)

    with Live() as live:
        live.log_artifact(
            str(models_path),
            type="model",
            name="beans_classifier",
            desc="Simple and fast dry bean classifier.",
            labels=["svc", "classification", "bean"]
        )
        logging.info("Model tracked with DVC.")


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    train_model(config_path=args.config)
