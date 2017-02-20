# app.py

import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, escape, jsonify
from extensions import mysql
from flask_restful import Resource, Api
import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')
api = Api(app)

# Initialize MySQL database connector
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'eecs481' ##???
mysql.init_app(app)

# Super secret key   ??????
app.secret_key = "<}2[\xb6f\x97\xf1\\%\x15\x99\xfa\x93@\xec\xd0=\x9a\xb5d\xe3\x92\x9c\x01<"

# Register the controllers
app.register_blueprint(controllers.index)
app.register_blueprint(controllers.signup)
app.register_blueprint(controllers.dashboard)
app.register_blueprint(controllers.notes)
app.register_blueprint(controllers.contacts)
app.register_blueprint(controllers.vitals)

class HelloWorld(Resource):
    def get(self):
        return jsonify(hello='world')

api.add_resource(HelloWorld, '/getNote')



# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
    # listen on external IPs
    app.run(host='0.0.0.0', port=3000, debug=True)