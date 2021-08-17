from sqlite3 import connect, Error

database = "database/db.sqlite"

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_query):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_query)
    except Error as e:
        print(e)