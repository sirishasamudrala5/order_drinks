import pymysql

_connection = None

def get_connection():
    global _connection
    if not _connection:
        _connection = pymysql.connect(host='<db-host>',port=3306,user='<db-user>', password='<password>',db='<db-name>', charset='utf8')
    cursor = _connection.cursor()
    return cursor

# List of stuff accessible to importers of this module. Just in case
__all__ = ['get_connection']
