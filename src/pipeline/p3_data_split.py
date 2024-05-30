import argparse
import logging

import yaml
from pandas import read_csv

from components.svc_model_trainer import SVCModelTrainer
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
    data = read_csv(features_path)

    model_trainer = SVCModelTrainer()

    logging.info("Data split.")
    train_dataset, test_dataset = model_trainer.split_train_test_data(
        data=data,
        test_size=config['data_split']['test_size'])

    logging.info("Feature scaling.")
    model_trainer.scale_features(
        train_dataset=train_dataset,
        test_dataset=test_dataset)

    logging.info("Trying to save train and test datasets.")
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
