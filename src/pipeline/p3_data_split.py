import argparse
import logging

import pandas as pd
import yaml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from entity.bean import BeanProperties as bp
from utils.dir_utils import DirUtils


def data_split(config_path: str) -> None:
    """Split dataset into train/test.
    Args:
        config_path {str}: Path to yaml configuration file.
    """

    logging.info("Stage 3: data split.")

    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)

    logging.info("Reading featurized dataset.")
    features_path = config['featurize']['features_path']
    data = pd.read_csv(features_path)

    # Data split
    logging.info("Data split.")
    train_dataset, test_dataset = train_test_split(
        data,
        test_size=config['data_split']['test_size'],
        random_state=config['base']['random_state'],
        shuffle=True)

    # Feature Scaling
    logging.info("Feature scaling.")
    columns: list[str] = train_dataset.columns.drop(bp.clazz).to_list()

    standard_scaler = StandardScaler()
    train_dataset[columns] = pd.DataFrame(
        standard_scaler.fit_transform(train_dataset[columns]),
        index=train_dataset.index)

    # Save datasets
    try:
        train_csv_path = config['data_split']['trainset_path']
        test_csv_path = config['data_split']['testset_path']

        DirUtils.exists_else_create_dir(train_csv_path)
        DirUtils.exists_else_create_dir(test_csv_path)

        train_dataset.to_csv(train_csv_path, index=False)
        test_dataset.to_csv(test_csv_path, index=False)
        logging.info(
            f"CSV files created successfully in {train_csv_path} and {test_csv_path}.")
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    data_split(config_path=args.config)
