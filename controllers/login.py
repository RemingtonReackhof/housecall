# login.py

from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid


login = Blueprint('login', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


@login.route('/login', methods=['GET', 'POST'])
def login_route():

	# if "username" in session:
	# 	return redirect(url_for('user.user_edit_route'))

	# prevURL = request.referrer

	if request.method == 'POST':
		print "here"
		emailIn = request.form['email']
		passIn = request.form['password'] #get input
		#prevURL = request.form.get("prevURL") #redirect address

		# Check if Emt or Doctor
		Emt = request.form['emt_button']
		Doctor = request.form['doctor_button']

		#Check if username exists
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM eecs481.Emt WHERE email = '"+emailIn+"'")
		email = cur.fetchall()
		if len(email) == 0:
			flash("Incorrect email", "error_email")
			return redirect(url_for('login.login_route'))

		#Salt and hash check
		# algorithm = 'sha512'

		# user_pass = username[0][3] #usernames password info
		# user_pass = user_pass.split('$')

		# m = hashlib.new(algorithm)
		# m.update(user_pass[1] + passIn)
		# password_hash = m.hexdigest()

		# #Check if passed in password matches actual password
		# if password_hash != user_pass[2]:
		# 	flash("Incorrect username/password combination", "error_combo")
		# 	return redirect(url_for('login.login_route'))

		if passIn != email[0][4]:
			flash("Incorrect email/password combination", "error_combo")
			return redirect(url_for('login.login_route'))

		#if user/pass is valid
		session['email'] = email[0][0] 
		session['skype_username'] = email[0][1]
		session['firstname'] = email[0][2]
		session['lastname'] = email[0][3]

		#if prevURL != None:
			#return redirect(prevURL)
		return redirect(url_for('main.main_route')) #FIGURE OUT ESCAPE SESSION

	return render_template("login.html")

