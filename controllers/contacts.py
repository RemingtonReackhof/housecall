from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid
import ast
import datetime


contacts = Blueprint('contacts', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


@contacts.route('/contacts', methods=['GET', 'POST'])
def my_route():

	# if not logged in
	username = request.args.get("username")
	if username is None:    
		if "username" not in session:
			return redirect(url_for("index.index_route"))
		username = session['username']


	return render_template("index.html", name='contacts')


@contacts.route('/contacts-info', methods=['GET'])
def my_route_1():

	if request.method == 'GET':

		# Retrieve all the doctors to display on Contacts page

		cur = mysql.connection.cursor()
		cur.execute("SELECT user_id, skype_username, firstname, lastname, specialty FROM User WHERE Doctor = 1;")
		rows = cur.fetchall()
		
		if rows is None:
			return jsonify(successful=False)
		else:
			return jsonify(successful=True, rows=rows)


@contacts.route('/contacts-call', methods=['POST'])
def my_route_2():

	if request.method == 'POST':

		data = ast.literal_eval(request.data)  # emtUsername and dr_id

		# Get EMT's ID using their username
		emtUsername = data[0]
		cur = mysql.connection.cursor()
		cur.execute("SELECT user_id FROM User WHERE skype_username = %s AND Doctor = 0;", emtUsername)
		emt_id = cur.fetchone()

		# Get timestamp
		timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

		# Insert new row for this call into Call table
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO Call (emt_id, dr_id, time_stamp, call_length) VALUES (%s, %s, %s, %s)", [ emt_id, data[1], timestamp, str(0) ])
		mysql.connection.commit()

		# Get this call's call_id
		cur = mysql.connection.cursor()
		cur.execute("SELECT call_id FROM Call ORDER BY call_id DESC LIMIT 1;")
		callID = cur.fetchone()

		# Return JSON with call id to Garett
		return jsonify(successful=True, callID=callID)

		#return render_template("index.html", name='notes')

