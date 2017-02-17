from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid


index = Blueprint('index', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")

@index.route('/', methods=['GET', 'POST'])
def index_route():

	if "username" in session:
	 	return redirect(url_for('main.main_route'))    ### Have to change

	prevURL = request.referrer

	if request.method == 'POST':
		print "here"
		emailIn = request.form['email']
		passIn = request.form['password'] #get input

		prevURL = request.form.get("prevURL") #redirect address

		# Check if Emt or Doctor
		#Emt = request.form['emt_button']
		#Doctor = request.form['doctor_button']

		#Check if username exists
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM eecs481.User WHERE email = '"+emailIn+"'")
		email = cur.fetchall()
		#print email
		if len(email) == 0:
			print "wrong email"
			flash("Incorrect email", "error_email")
			return redirect(url_for('index.index_route'))

		#Salt and hash check
		algorithm = 'sha512'

		user_pass = email[0][5] #usernames password info
		print email[0]
		print "USER_PASS", user_pass
		user_pass = user_pass.split('$')

		m = hashlib.new(algorithm)
		m.update(user_pass[1] + passIn)
		password_hash = m.hexdigest()
		print "PASSWORD_HASH", password_hash
		print "USER_PASS[2]", user_pass[2]

		#Check if passed in password matches actual password
		if password_hash != user_pass[2]:
			flash("Incorrect username/password combination", "error_combo")
			return redirect(url_for('index.index_route'))

		# if passIn != email[0][5]:
		# 	print "wrong password"
		# 	flash("Incorrect email/password combination", "error_combo")
		# 	return redirect(url_for('index.index_route'))

		#if user/pass is valid
		session['email'] = email[0][1] 
		session['skype_username'] = email[0][2]
		session['firstname'] = email[0][3]
		session['lastname'] = email[0][4]
		session['specialty'] = email[0][6]
		session['hospital_id'] = email[0][7]
		session['dr_or_emt'] = email[0][8]

		print prevURL
		if prevURL != None:
			return redirect(prevURL)
		return redirect(url_for('main.main_route'))

	return render_template("index.html", prevURL=prevURL)
