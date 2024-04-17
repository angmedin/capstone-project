from typing import Any, Dict, List

import mysql.connector as mysqlc
from mysql.connector.connection import MySQLConnection
from mysql.connector.types import RowItemType, RowType

from common.logger import Logger


class MySQLQueryEngine:
    """
    Establishes a connection to a MySQL database and executes queries.
    """

    def __init__(self,
                 host='localhost',
                 user='dry_bean_user',
                 password='dry_bean_user_password',
                 database='dry_bean'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.logger = Logger()

    def connect(self) -> MySQLConnection | None:
        try:
            self.connection = mysqlc.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.logger.log_info("Connection established")
        except mysqlc.Error as err:
            self.logger.log_error(
                f"Connection could not be established {err.msg}")

        return self.connection

    def execute_query(self, query: str) -> List[RowType | Dict[str, RowItemType]] | Any:
        if not self.connection:
            self.logger.log_error("A MySQL connection is required")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysqlc.Error as err:
            self.logger.log_error(
                f"Could not execute the query: {query}. Reason: {err.msg}")

    def close(self) -> None:
        if self.connection:
            self.connection.close()
            self.logger.log_info("Connection closed")
