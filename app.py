# app.py

import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, escape
from extensions import mysql
import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

# Initialize MySQL database connector
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'eecs481' ##???
mysql.init_app(app)

# Super secret key   ??????
app.secret_key = "<}2[\xb6f\x97\xf1\\%\x15\x99\xfa\x93@\xec\xd0=\x9a\xb5d\xe3\x92\x9c\x01<"

# Register the controllers
app.register_blueprint(controllers.login) #, url_prefix="/04d8ee3a8730446aa2b4/pa3")
app.register_blueprint(controllers.user) #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3000, debug=True)