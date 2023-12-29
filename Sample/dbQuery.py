import traceback

from .dbConnHelper import init_connection_engine
from ..models import queryModel
import sqlalchemy

db = None
def getDb():
    global db
    db = db or init_connection_engine()
    return db

def execQuery(param):
    db = getDb()
    try:
        #stmt = sqlalchemy.text(param.query)    
        connection = db.connect()
        result = connection.execute(param)
        connection.close()                
        return result
    except Exception as e:
        print(str(e))
        return "Exception"


def execQueryRaw(param: queryModel.GetQuery):
    db = getDb()
    try:
        stmt = sqlalchemy.text(param.query)
        with db.connect() as conn:
            result = conn.execute(stmt)
        return result
    except Exception as e:
        return "Exception"


def execOptimizedQueryRaw(param: queryModel.GetQuery):
    db = getDb()
    try:
        stmt = sqlalchemy.text(param.query)
        with db.connect() as conn:
            result = conn.execute(stmt)
        return result , None
    except Exception as e:
        print(str(e))
        print(traceback.print_exc())
        return "Exception" , e