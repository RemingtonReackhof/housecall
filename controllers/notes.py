from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid
import ast


notes = Blueprint('notes', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


@notes.route('/notes', methods=['GET', 'POST'])
def my_route():

	if request.method == 'GET':
		print 'GETTING'
		return render_template("index.html", name='notes')

	if request.method == 'POST':
		print 'POSTING'
		return jsonify(message="Success!") 

	return render_template("index.html", name="notes")