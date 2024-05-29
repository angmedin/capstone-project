import logging

from pandas import DataFrame, read_sql

from components.mysql_query_engine import MySQLQueryEngine
from entity.bean import BeanProperties as bp


class DataReporter():
    def __init__(self) -> None:
        self.query_engine = MySQLQueryEngine()
        self.mysql_connection = self.query_engine.connect()

    def __del__(self) -> None:
        if self.mysql_connection and self.mysql_connection.is_connected():
            self.mysql_connection.close()

    def get_all_bean_data(self) -> DataFrame | None:
        query = """
            SELECT * FROM bean
        """

        if self.mysql_connection is None:
            logging.error("Aborting data fetch. No connection available.")
            return None

        try:
            df = pd.read_sql(sql=query, con=self.mysql_connection)
            return df
        except Exception as ex:
            logging.error(f"Error while fetching: {ex}")

        return None

    def get_filtered_bean_data(self) -> DataFrame | None:
        query = f"""
            SELECT  {bp.area}, {bp.perimeter}, {bp.major_axis_length}, 
                    {bp.minor_axis_length}, {bp.aspect_ration}, {bp.eccentricity}, 
                    {bp.convex_area}, {bp.equiv_diameter}, {bp.extent}, 
                    {bp.solidity}, {bp.roundness}, {bp.compactness}, {bp.shape_factor_1}, 
                    {bp.shape_factor_2}, {bp.shape_factor_2}, {bp.shape_factor_3}, 
                    {bp.shape_factor_4}, {bp.clazz}
            FROM 
                bean
            WHERE
                    {bp.eccentricity} >= 0.3
                AND {bp.convex_area} <= 250000
                AND {bp.solidity} >= 0.94
                AND {bp.roundness} >= 0.51
                AND {bp.shape_factor_1} <= 0.0104
                AND {bp.shape_factor_4} >= 0.954
        """

        if self.mysql_connection is None:
            logging.error("Aborting data fetch. No connection available.")
            return None

        try:
            df = read_sql(sql=query, con=self.mysql_connection)
            return df
        except Exception as ex:
            logging.error(f"Error while fetching: {ex}")

        return None
