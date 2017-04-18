# signup.py

from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid


signup = Blueprint('signup', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


@signup.route('/signup', methods=['GET', 'POST'])
def signup_route():

	if 'username' in session:
		return redirect(url_for('main.main_route'))

	prevURL = request.referrer
	
	if request.method == 'POST':

		try:
			emailIn = request.json.get('email')
		except:
			print "error"

		
		# Get all user information
		skypeUsernameIn = request.json.get('skype_username')
		passIn = request.json.get('password')
		firstnameIn = request.json.get('firstname')
		lastnameIn = request.json.get('lastname')
		hospitalIn = request.json.get('hospital')
		specialtyIn = request.json.get('specialty')
		doctorIn = request.json.get('doc')


		# Get Hospital Id
		cur = mysql.connection.cursor()
		cur.execute("SELECT hospital_id FROM Hospital WHERE name = %s", [hospitalIn])
		hospitalIdIn = cur.fetchone()


		#Salt and hash password
		algorithm = 'sha512'
		salt = uuid.uuid4().hex

		m = hashlib.new(algorithm)
		m.update(salt + passIn)
		password_hash = m.hexdigest()

		password = "$".join([algorithm,salt,password_hash])


		#Insert user into table
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO User (email, skype_username, firstname, lastname, password, specialty, hospital_id, Doctor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [emailIn, skypeUsernameIn, firstnameIn, lastnameIn, password, specialtyIn, hospitalIdIn, doctorIn])
		mysql.connection.commit()


		usertype = 'emt'
		if doctorIn == '1':
			usertype = 'dr'

		return jsonify(message="Success!", username=emailIn, user_type=usertype) 


	return render_template("index.html", name="signup")
