import psycopg2 from psycopg2.extras 
import RealDictCursor

_connection = None

def get_connection():
    global _connection
    if not _connection:
         _connection = psycopg2.connect("host='localhost' dbname='nearmegala' user='nearme' password='nearme'")   
         _cursor = _connection.cursor(cursor_factory=RealDictCursor)
    return _cursor

# List of stuff accessible to importers of this module. Just in case
__all__ = ['get_connection']