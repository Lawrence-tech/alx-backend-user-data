#!/usr/bin/env python3
"""
Module for database connection.
"""

import os
import mysql.connector


def get_db():
    """
    Create a connection to the MySQL db using env variables for credentials

    Returns:
        mysql.connector.connection.MySQLConnection: The db connection object.
    """
    username = os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME')

    db = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )

    return db
