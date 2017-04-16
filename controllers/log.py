from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid
import ast


log = Blueprint('log', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


@log.route('/log', methods=['GET'])
def my_route():

	# if not logged in
	username = request.args.get("username")
	if username is None: 
		if "username" not in session:
			return redirect(url_for("index.index_route"))
		username = session['username']

	if len(request.args) == 0:
			return render_template("index.html", name="notes")

	content = {}
	user_id = request.args['user_id']
	user_type = request.args['user_type']
	toSend = []
	cur = mysql.connection.cursor()

	if user_type == 'emt':
		cur.execute("SELECT call_id, emt_id, dr_id, time_stamp, call_length, is_active FROM `Call` WHERE emt_id="+user_id+";")
		content = cur.fetchall()

	elif user_type == 'dr':
		cur.execute("SELECT call_id, emt_id, dr_id, time_stamp, call_length, is_active FROM `Call` WHERE dr_id = '"+str(user_id)+"'")
		content = cur.fetchall() 


	if content is not None:
		for item in content:
			cur.execute("SELECT * FROM User WHERE user_id  = '"+str(item[2])+"'")
			dr = cur.fetchone()
			cur.execute("SELECT * FROM User WHERE user_id  = '"+str(item[1])+"'")
			emt = cur.fetchone()
			#TODO: fix this
			toSend.append({'call_id':item[0], 'emt_id': emt, 'dr_id': dr, 'timestamp':item[3], 'call_length':item[4], 'is_active':item[5]})
		print content


	return jsonify(successful=True, content=toSend)

