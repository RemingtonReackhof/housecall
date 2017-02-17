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
	print "at signup route"
	if request.method == 'POST':

		print "post"
		# try:
		# 	print request.form
		# 	emailIn = request.form['email']
		# except:
		# 	print "error"
		# skypeUsernameIn = request.form['skype_username']
		# passIn = request.form['password']
		# firstnameIn = request.form['firstname']
		# lastnameIn = request.form['lastname']

		emailIn = "email@umich.edu"
		skypeUsernameIn = "username"
		passIn = "ppppp"
		firstnameIn = "greatest"
		lastnameIn = "ever"
		hospitalIn = "Med Inn Building"
		specialtyIn = "Neurology"
		doctorIn = True

		#print emailIn, skypeUsernameIn, passIn, firstnameIn, lastnameIn

		# Get Hospital Id
		cur = mysql.connection.cursor()
		cur.execute("SELECT hospital_id FROM eecs481.Hospital WHERE name =  '"+hospitalIn+"'")
		hospitalIdIn = cur.fetchall()


		# They'll click one of two buttons indicating if they are doctor or emt

		# Hospital will have to be one from a drop down list

		#specialtyIn = request.form['specialty']

		#Salt and hash password
		algorithm = 'sha512'
		salt = uuid.uuid4().hex

		m = hashlib.new(algorithm)
		m.update(salt + passIn)
		password_hash = m.hexdigest()

		password = "$".join([algorithm,salt,password_hash])

		#Insert user into table
		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO eecs481.User (email, skype_username, firstname, lastname, password, specialty, hospital_id, Doctor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [emailIn, skypeUsernameIn, firstnameIn, lastnameIn, password, specialtyIn, hospitalIdIn, doctorIn])
		mysql.connection.commit()

		#Redirect to /login to try new credentials!
		prevURL = request.form.get("prevURL") #redirect address
		#return redirect(redirect_url())
		return redirect(url_for("index.index_route"))


	return render_template("signup.html")