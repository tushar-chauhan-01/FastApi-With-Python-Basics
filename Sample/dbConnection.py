import sqlalchemy
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv 
load_dotenv(os.path.join(BASE_DIR, "helpers", ".env"))

def init_connection_engine():
    db_config = {
        "pool_size": 5,
        "max_overflow": 2,
        "pool_timeout": 30,
        "pool_recycle": 1800,
    }
    return init_unix_connection_engine(db_config)


def init_unix_connection_engine(db_config):
    # db_socket_dir = os.getenv("DB_SOCKET_DIR", "/cloudsql")
    # db_user = secrets_manager.get_secret(SecretManagerConstants.CLOUD_SQL_USERNAME)
    # db_pass = secrets_manager.get_secret(SecretManagerConstants.CLOUD_SQL_PASSWORD)
    # db_name = secrets_manager.get_secret(SecretManagerConstants.AUTH_CLOUD_SQL_DATABASE_NAME)
    # cloud_sql_connection_name = secrets_manager.get_secret(SecretManagerConstants.CLOUD_SQL_CONNECTION_NAME)
    # pool = sqlalchemy.create_engine(
    #     sqlalchemy.engine.url.URL(
    #         drivername="mysql+pymysql",
    #         username=db_user,
    #         password=db_pass,
    #         database=db_name,
    #         query={
    #             "unix_socket": "{}/{}".format(
    #                 db_socket_dir,
    #                 cloud_sql_connection_name)
    #         }
    #     ),
    #     **db_config
    # )
    pool = sqlalchemy.create_engine('mysql+pymysql://root:hbhhknkbs@localhost/dev-backend')
    return pool