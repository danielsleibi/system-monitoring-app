import mysql.connector
from mysql.connector import Error
from modules.usage import *
from os import environ

# database information
# retrieved from enivorment variable or default if does not exists
DB_HOST = environ.get('DB_HOST', "172.17.0.1")
DB_NAME = environ.get("DB_NAME", "system_data")
DB_PORT = environ.get("DB_PORT", "13306")
DB_USER = environ.get("DB_USER", "root")
DB_PASSWORD = environ.get("DB_PASSWORD", "12345")

if __name__ == "__main__":
    cpu_util = get_cpu_util()
    disk_usage = get_disk_usage()
    memory_usage = get_memory_usage()

    try:
        connection = mysql.connector.connect(host=DB_HOST, port=DB_PORT,
                                             database=DB_NAME,
                                             user=DB_USER,
                                             password=DB_PASSWORD)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(
                f"INSERT INTO cpu_usage VALUES(CURRENT_TIMESTAMP(), {cpu_util['utilization']});")
            cursor.execute(
                f"INSERT INTO disk_usage VALUES(CURRENT_TIMESTAMP(), {disk_usage['total']}, {disk_usage['used']});")
            cursor.execute(
                f"INSERT INTO memory_usage VALUES(CURRENT_TIMESTAMP(), {memory_usage['total']}, {memory_usage['used']});")
            connection.commit()
            print("SAVED DATA")
            print(f"[CPU: {cpu_util['utilization']}], [DISK: total:{disk_usage['total']}, used:{disk_usage['used']}], [MEMORY: total:{memory_usage['total']}, used:{memory_usage['used']}]")
            # logger.debug("Data: %s", records)
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # closing database connection.
        if connection.is_connected():
            cursor.close()
            connection.close()
