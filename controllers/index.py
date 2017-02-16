from flask import *
from extensions import mysql

index = Blueprint('index', __name__, template_folder='templates')

@index.route("/")
def index_route():
	return render_template("index.html")
