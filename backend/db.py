import pymysql

_connection = None

def get_connection():
    global _connection
    if not _connection:
        _connection = pymysql.connect(host='localhost',port=3306,user='root', password='chikkIbuddI57',db='drinks', charset='utf8')
    cursor = _connection.cursor()
    return cursor

# List of stuff accessible to importers of this module. Just in case
__all__ = ['get_connection']
