from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid
import ast


contacts = Blueprint('contacts', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


@contacts.route('/contacts', methods=['GET', 'POST'])
def my_route():
	#print 'GETTING'


	# if not logged in
	username = request.args.get("username")
	if username is None:    
		if "username" not in session:
			return redirect(url_for("index.index_route"))
		username = session['username']



	# if request.method == 'GET':
	# 	print "contacts getting"
	# 	cur = mysql.connection.cursor()
	# 	cur.execute("SELECT user_id, skype_username, firstname, lastname, specialty FROM User WHERE Doctor = 1;")
	# 	rows = cur.fetchall()
	# 	print rows
	# 	if rows is None:
	# 		return jsonify(successful=False)
	# 	else:
	# 		return jsonify(successful=True, rows=rows)


	if request.method == 'POST':

		data = ast.literal_eval(request.data)

		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO Call (emt_id, dr_id, time_stamp, call_length) VALUES (%s, %s, %s, %s)", [ data['emt_id'], data['dr_id'], data['time_stamp'], data['call_length'] ])
		mysql.connection.commit()

		return render_template("index.html", name='notes')



	return render_template("index.html", name='contacts')


@contacts.route('/contacts-info', methods=['GET'])
def my_route_1():

	if request.method == 'GET':
		print "contacts getting"
		cur = mysql.connection.cursor()
		cur.execute("SELECT user_id, skype_username, firstname, lastname, specialty FROM User WHERE Doctor = 1;")
		rows = cur.fetchall()
		print rows
		if rows is None:
			return jsonify(successful=False)
		else:
			return jsonify(successful=True, rows=rows)

	