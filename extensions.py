from flask_mysqldb import *

# Create MySQL object. We create it here to avoid
# circular dependencies that would occur if we created in
# app.py
mysql = MySQL()
