from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid
import ast


contacts = Blueprint('contacts', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


@contacts.route('/contacts', methods=['GET'])
def my_route():
	#print 'GETTING'

	# if not logged in
	username = request.args.get("username")
	if username is None:    
		if "username" not in session:
			return redirect(url_for("index.index_route"))
		username = session['username']

	return render_template("index.html", name='contacts')