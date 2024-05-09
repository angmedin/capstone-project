import logging
import os

from api.exception import DirectoryCreateException


class DirUtils():

    @staticmethod
    def exists_else_create_dir(path: str) -> None:
        """If the specified directory does not exist then it 
        is created.

        Args:
            path (str): Relative directory path. 

        Raises:
            DirectoryCreateException: Raised when the directory couldn't be created.
        """
        try:
            sub_directories = path.split(sep='/')

            if '.' in path:
                # Take all the subdirectories except the last one when the leaf is the file name.
                sub_directories = sub_directories[:-1]

            # Join the subdirectories to build the relative path
            relative_path = './'.join(sub_directories)

            if not os.path.exists(f"./{relative_path}"):
                os.makedirs(f"./{relative_path}")

        except Exception as e:
            logging.error(e)
            raise DirectoryCreateException("Couldn't create directory.")
