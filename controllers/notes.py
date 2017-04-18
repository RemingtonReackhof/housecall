from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
from werkzeug.utils import secure_filename
import hashlib
import uuid
import ast
import os


notes = Blueprint('notes', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = "static/images/"

def allowed_file(filename):
    if '.' in filename:
    	if filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
    		return True
    return False


@notes.route('/notes', methods=['GET', 'POST'])
def my_route():

	# # if not logged in
	# username = request.args.get("username")
	# if username is None: 
	# 	if "username" not in session:
	# 		return redirect(url_for("index.index_route"))
	# 	username = session['username']


	# Get callID regardless
	user = session['skype_username']
	cur = mysql.connection.cursor()
	cur.execute("SELECT user_id FROM User WHERE skype_username = (%s)", [user])
	userID = cur.fetchone()[0]
	cur = mysql.connection.cursor()
	cur.execute("SELECT `call_id` FROM `Call` WHERE `emt_id` = '"+str(userID)+"' OR `dr_id` = '"+str(userID)+"' ORDER BY `call_id` DESC LIMIT 1")
	callID = cur.fetchall()[0][0]
	print callID

	if request.method == 'GET':
		if len(request.args) == 0:
			return render_template("index.html", name="notes")

		#print 'GETTING'
		content = {}
		note_id = request.args['note_id']
		toSend = []


		if note_id == '1':
			print 'note id is 1'
			note_id = int(note_id)
			note_id = 1
			cur = mysql.connection.cursor()
			#cur.execute("SELECT note_id,content,time_stamp, is_note, is_instruction, is_image FROM Notes WHERE note_id > '"+str(note_id)+"'")
			cur.execute("SELECT note_id,content,time_stamp, is_note, is_instruction, is_image FROM Notes WHERE call_id = '"+str(callID)+"'")
			content = cur.fetchall()
			if content is not None:
				num_notes = len(content)
				for i in range(0,num_notes):
					toSend.append({'content':content[i][1], 'time_stamp':content[i][2], 'note_id':content[i][0], 'is_note':content[i][3], 'is_instruction':content[i][4], 'is_image':content[i][5]})
				print content

		else:
			print 'note id is greater than 1'
			cur = mysql.connection.cursor()
			#cur.execute("SELECT note_id,content,time_stamp, is_note, is_instruction, is_image FROM Notes WHERE note_id = '"+note_id+"'")
			cur.execute("SELECT note_id,content,time_stamp, is_note, is_instruction, is_image FROM Notes WHERE note_id = '"+note_id+"' AND call_id = '"+str(callID)+"'")
			content = cur.fetchone()
			if content is not None:
				toSend.append({'content':content[1], 'time_stamp':content[2], 'note_id':content[0], 'is_note':content[3], 'is_instruction':content[4], 'is_image':content[5]})
			print content

		if content is None and len(toSend) == 0:
			return jsonify(successful=False)
		else:
			return jsonify(successful=True, content=toSend)


	if request.method == 'POST':	

		# If data is a Note or Instruction
		if not request.files:

			data = ast.literal_eval(request.data)
			
			if(data['messageTitle'] == ""):
				data['messageTitle'] = "no title"

			cur = mysql.connection.cursor()
			cur.execute("INSERT INTO Notes (is_note, is_instruction, is_image, title, time_stamp, content, call_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", [ True if data['isNote'] == 'true' else False, True if data['isInstruction'] == 'true' else False, True if data['isImage'] == 'true' else False, data['messageTitle'], data['messageTime'], data['messageContent'], str(callID) ])
			mysql.connection.commit()

			cur.execute("SELECT note_id FROM Notes WHERE content = %s", [data['messageContent']])
			recent_note_id = max(cur.fetchall())
		
			return jsonify(note_id=recent_note_id) 


		# If data is an Image
		else:
			
			# check if the post request has the file part
			if 'file' not in request.files:
				return redirect(request.url)
			file = request.files['file']

			# if user does not select file, browser also
			# submit a empty part without filename
			if file.filename == '':
				return redirect(request.url)

			if file and allowed_file(file.filename):

				filename = secure_filename(file.filename)
				name_of_file = UPLOAD_FOLDER + filename
				file.save(name_of_file)

				cur = mysql.connection.cursor()
				cur.execute("INSERT INTO Notes (is_note, is_instruction, is_image, title, time_stamp, content, call_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", [ False, False, True, filename, '0:00', filename , str(callID)])
				mysql.connection.commit()

				cur.execute("SELECT note_id FROM Notes WHERE content = %s", [filename])
				recent_note_id = max(cur.fetchall())

				#return render_template("index.html", name="notes")
				return redirect("/notes", code=302)
				#return redirect(url_for(notes.my_route))


	return render_template("index.html", name="notes")


@notes.route('/notes-endcall', methods=['POST'])
def my_route_1():

	# Get callID
	# user = session['skype_username']
	# cur = mysql.connection.cursor()
	# cur.execute("SELECT user_id FROM User WHERE skype_username = (%s)", [user])
	# userID = cur.fetchone()[0]

	userID = request.form['userID']
	cur = mysql.connection.cursor()
	cur.execute("SELECT `call_id` FROM `Call` WHERE `emt_id` = '"+str(userID)+"' OR `dr_id` = '"+str(userID)+"' ORDER BY `call_id` DESC LIMIT 1")
	callID = cur.fetchall()[0][0]
	print callID


	# Update Call table to make this call inactive
	cur = mysql.connection.cursor()
	cur.execute("UPDATE `Call` SET `is_active` = 0 WHERE `call_id` = '"+str(callID)+"'")
	mysql.connection.commit()


	# Redirect to dashboard
	return jsonify(successful=True)
