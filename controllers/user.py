from flask import *
from extensions import mysql
import re
import hashlib
import uuid

user = Blueprint('user', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")


