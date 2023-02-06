# -*- coding: utf-8 -*-

import os
import contextlib
import sqlite3
import pathlib
import pandas as pd


DATABASE_FILE = os.getenv("DATABASE_FILE")


@contextlib.contextmanager
def open_sqlite(db_file: str) -> None:
    """Context manager to open a SQLite database and handle exceptions.

    Args:
        db_file: The SQLite database file to be queried.

    """
    conn = sqlite3.connect(db_file)
    try:
        yield conn
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()


def query_sqlite(
    query_string: str, db_file: pathlib.PosixPath = DATABASE_FILE
) -> pd.DataFrame:
    """Queries a SQLite database and returns the result as a Pandas DataFrame.

    Args:
        query_string: The SQL query to be executed.
        db_file (optional): The SQLite database file to be queried. Defaults to the value of the environment variable `DATABASE_FILE`.

    """
    with open_sqlite(db_file) as conn:
        return pd.read_sql_query(
            query_string,
            conn,
        )


def export_image(picture_id: str, db_file: pathlib.PosixPath = DATABASE_FILE) -> None:
    """Exports an image from a SQLite database based on the specified selection criteria.

    Args:
        picture_id: ID of the image to be exported.
        db_file (optional): The SQLite database file to be queried. Defaults to the value of the environment variable `DATABASE_FILE`.

    """
    with open_sqlite(db_file) as conn:
        cursor = conn.cursor()
        query = f"SELECT * FROM picture WHERE picture_id = '{picture_id}';"
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
            image = row[5]
            with open(".image.jpg", "wb") as file:
                file.write(image)
