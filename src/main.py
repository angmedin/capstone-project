from components.data_reporter import DataReporter
from common.logger import Logger


def start() -> None:
    Logger.setup()

    dr = DataReporter()
    df = dr.get_filtered_bean_data()
    print(df.head())

if __name__ == '__main__':
    start()
