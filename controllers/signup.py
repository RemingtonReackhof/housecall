# signup.py

from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid


signup = Blueprint('signup', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


@signup.route('/signup', methods=['GET', 'POST'])
def signup_route():




	return render_template("signup.html")