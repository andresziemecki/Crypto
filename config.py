from logging import basicConfig, INFO, error
from database.sql import create_connection, create_table, database
from database.tickers import sql_create_tickers_table


def setConfig():

    setLoggingConfig()
    conn = setDBConfig()
    return conn

def setLoggingConfig():
    basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level= INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

def setDBConfig():
    

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_tickers_table)
        return conn

    else:
        logError("Error! cannot create the database connection.")


def logError(s):
    error("Error! cannot create the database connection.")