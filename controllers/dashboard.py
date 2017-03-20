from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid
import ast


dashboard = Blueprint('dashboard', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


@dashboard.route('/dashboard', methods=['GET'])
def my_route():
	#print 'GETTING'

	username = request.args.get("username")
	if username is None:    
		if "username" not in session:
			return redirect(url_for("index.index_route"))
		username = session['username']

	return render_template("index.html", name='dashboard')

# @dashboard.route('/logout', methods=['GET', 'POST'])
# def my_logout():
# 	if request.method == 'POST':
# 		session.clear()
# 		return redirect(url_for('index.my_route'))