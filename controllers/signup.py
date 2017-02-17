# signup.py

from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid


signup = Blueprint('signup', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


@signup.route('/signup', methods=['GET', 'POST'])
def signup_route():

	prevURL = request.referrer

	if request.method == 'POST':

		emailIn = request.form['email']
		skypeUsernameIn = request.form['skypeUsername']
		passIn = request.form['password']
		firstnameIn = request.form['firstname']
		lastnameIn = request.form['lastname']

		# They'll click one of two buttons indicating if they are doctor or emt

		# Hospital will have to be one from a drop down list

		specialtyIn = request.form['specialty']


		prevURL = request.form.get("prevURL") #redirect address


	return render_template("signup.html")