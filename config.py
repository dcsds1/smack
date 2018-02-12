import os


DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'your-user-name'
PASSWORD = 'your-password'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'your-database-name'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset:utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
