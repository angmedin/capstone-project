from components.data_reporter import DataReporter


def start() -> None:
    dr = DataReporter()
    dr.get_filtered_bean_data()


if __name__ == '__main__':
    start()
