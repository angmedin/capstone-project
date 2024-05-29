import argparse
import logging

import yaml
from pandas import DataFrame, read_csv

from components.svc_model_trainer import SVCModelTrainer
from utils.dir_utils import DirUtils


def featurize(config_path: str) -> None:
    """Clean features and encode categorical feature `class`.
    Args:
        config_path {str}: Path to yaml configuration file.
    """

    logging.info("Stage 2: featurize.")

    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)

    logging.info("Reading prepared dataset.")
    raw_data: DataFrame = read_csv(config['data_load']['dataset_prepare'])

    model_trainer = SVCModelTrainer()

    logging.info("Dropping unused columns.")
    data: DataFrame = model_trainer.drop_columns(data=raw_data)

    logging.info("Encoding categorical feature.")
    model_trainer.encode_labels(data=data)

    try:
        file_path = config['featurize']['features_path']
        DirUtils.exists_else_create_dir(file_path)
        data.to_csv(file_path, index=False)
        logging.info(f"CSV file created successfully in {file_path}.")
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    try:
        featurize(config_path=args.config)
    except Exception as e:
        logging.error(e)
