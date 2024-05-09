import argparse
import logging

import pandas as pd
import yaml
from sklearn.preprocessing import LabelEncoder

from entity.bean import BeanProperties as bp
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
    raw_data = pd.read_csv(config['data_load']['dataset_prepare'])

    # Drop columns
    logging.info("Dropping unused columns.")
    cols_to_drop = [bp.area, bp.perimeter, bp.compactness, bp.shape_factor_3]
    data = raw_data.drop(columns=cols_to_drop)

    # Encode target labels with value between 0 and n_classes-1
    logging.info("Encoding categorical feature.")
    label_encoder = LabelEncoder()
    data[bp.clazz] = label_encoder.fit_transform(data[bp.clazz])

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
