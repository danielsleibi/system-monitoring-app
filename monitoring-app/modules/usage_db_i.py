# Usage database functions and classes used to access data in the usage statistics database
import mysql.connector
from mysql.connector import Error
from modules.log_wrap import *
from os import environ

# database information
# retrieved from enivorment variable or default if does not exists
DB_HOST = environ.get('DB_HOST', "0.0.0.0")
DB_NAME = environ.get("DB_NAME", "system_data")
DB_PORT = environ.get("DB_PORT", "3306")
DB_USER = environ.get("DB_USER", "root")
DB_PASSWORD = environ.get("DB_PASSWORD", "")

# tables, variable used in determining table name for each usage type
types = {"c":  "cpu_usage", "d": "disk_usage", "m": "memory_usage"}


@wrap(entering_get_usage, exiting)
def get_all_usage(type):
    if type not in types:
        raise ValueError(f"Invalid usage type available types are: {types}")
    try:
        connection = mysql.connector.connect(host=DB_HOST, port=DB_PORT,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {types[type]}")
            records = cursor.fetchall()
            column_names = [description[0]
                            for description in cursor.description]
            connection.commit()

    except Error as e:
        logger.error("Error while connecting to MySQL %s", e)
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
    return [dict(zip(column_names, r)) for r in records]


@wrap(entering_get_usage, exiting)
def get_usage(type, hour=None):
    if hour != None and type(hour) != int:
        raise TypeError("Incorrect type for hour parameter, must be: int")

    if type not in types:
        raise ValueError(f"Invalid usage type available types are: {types}")
    try:
        connection = mysql.connector.connect(host=DB_HOST, port=DB_PORT,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()
            cond = "WHERE DATE(time_taken) = CURRENT_DATE()"  # conditions
            if hour != None:
                cond += f" AND HOUR(time_taken) = '{hour:02d}'"
            query = f"SELECT * FROM {types[type]} {cond};"
            cursor.execute(query)
            records = cursor.fetchall()
            column_names = [description[0]
                            for description in cursor.description]
            connection.commit()
            # logger.debug("Data: %s", records)

    except Error as e:
        logger.error("Error while connecting to MySQL %s", e)
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
    return [dict(zip(column_names, r)) for r in records]


@wrap(entering, exiting)
def init():
    try:
        connection = mysql.connector.connect(host=DB_HOST, port=DB_PORT,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()
            cpu_usage_query = "SHOW TABLES LIKE 'cpu_usage';"
            disk_usage_query = "SHOW TABLES LIKE 'disk_usage';"
            memory_usage_query = "SHOW TABLES LIKE 'memory_usage';"
            cursor.execute(cpu_usage_query)
            result = cursor.fetchall()
            if not result:
                cursor.execute(
                    "CREATE TABLE cpu_usage(time_taken DATETIME NOT NULL PRIMARY KEY, utilization FLOAT);")
                logger.info("Created cpu_usage table")
            cursor.execute(disk_usage_query)
            result = cursor.fetchall()
            if not result:
                cursor.execute(
                    "CREATE TABLE disk_usage(time_taken DATETIME NOT NULL PRIMARY KEY, total FLOAT, used FLOAT);")
                logger.info("Created disk_usage table")
            cursor.execute(memory_usage_query)
            result = cursor.fetchall()
            if not result:
                cursor.execute(
                    "CREATE TABLE memory_usage(time_taken DATETIME NOT NULL PRIMARY KEY, total FLOAT, free FLOAT);")
                logger.info("Created memory_usage table")
            connection.commit()

    except Error as e:
        logger.error("Error while connecting to MySQL %s", e)
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
    logger.info("Setup DB")
