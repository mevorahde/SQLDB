import pyodbc
import os
from dotenv import load_dotenv
from pathlib import Path

# Activate '.env' file
load_dotenv()
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

server = os.getenv("server")
database = os.getenv("database")
username = os.getenv("username")
password = os.getenv("password")

conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};Trusted_Connection=yes;autocommit=True;')
cursor = conn.cursor()

# Insert a single record
insert_query = "INSERT INTO customers (customerUsername, customerPassword, customerKey, Result) VALUES (?, ?, ?, ?)"
values = ('value2', 4949494949494, 303030303030, 'value4')
cursor.execute(insert_query, values)

# Select all rows
cursor.execute('SELECT * FROM customers')

for row in cursor:
    print('row = %r' % (row,))

# Close the connection
cursor.commit()
cursor.close()
conn.close()
