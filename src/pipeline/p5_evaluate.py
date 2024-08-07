import argparse
import json
import logging

import yaml
from pandas import read_csv

from components.svc_model_trainer import SVCModelTrainer
from dvclive import Live
from utils.dir_utils import DirUtils


def evaluate_model(config_path: str) -> None:
    """Evaluate model.
    Args:
        config_path {str}: Path to yaml configuration file.
    """

    logging.info("Stage 5: evaluate.")

    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)

    logging.info("Loading test dataset.")
    test_dataset_path = config['data_split']['testset_path']
    test_df = read_csv(test_dataset_path)

    logging.info("Evaluating model.")
    model_trainer = SVCModelTrainer()
    model_path = config['train']['model_path']
    encoder_path = config['featurize']['encoder_path']
    report = model_trainer.evaluate_model(
        test_dataset=test_df, model_path=model_path, encoder_path=encoder_path)

    if report is None:
        logging.error("Couldn't generate report. Aborting.")
        return

    logging.info("Saving metrics.")
    reports_path = str(config['evaluate']['reports_dir'])
    metrics_path = str(config['evaluate']['metrics_file'])
    metrics_file_path = f"{reports_path}/{metrics_path}"

    try:
        DirUtils.exists_else_create_dir(reports_path)
        with open(metrics_file_path, 'w') as file:
            json.dump(report, fp=file)
        logging.info(f"CSV file created successfully in {metrics_file_path}.")
    except Exception as e:
        logging.error(e)

    logging.info("Logging metrics.")
    with Live() as live:
        live.log_metric("accuracy", report['accuracy'])
        live.log_metric("macro/precision", report['macro avg']['precision'])
        live.log_metric("macro/recall", report['macro avg']['recall'])
        live.log_metric("macro/f1-score", report['macro avg']['f1-score'])
        live.log_metric("macro/support", report['macro avg']['support'])


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    evaluate_model(config_path=args.config)
