import argparse
import logging

import yaml

from api.exception import DataPreparationException
from components.data_reporter import DataReporter
from utils.dir_utils import DirUtils


def data_load(config_path: str) -> None:
    """Load data from data source defined in DataReporter.

    Args:
        config_path (str): Path to yaml configuration file.
    """

    logging.info("Stage 1: data preparation.")

    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)

    data_reporter = DataReporter()
    file_path = config['data_load']['dataset_prepare']

    logging.info("Fetching data.")
    data = data_reporter.get_filtered_bean_data()

    if data is None:
        raise DataPreparationException("Couldn't fetch data from reporter.")

    try:
        DirUtils.exists_else_create_dir(file_path)
        data.to_csv(file_path, index=False)
        logging.info(f"CSV file created successfully in {file_path}.")
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)
