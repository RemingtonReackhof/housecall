from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid
import ast


notes = Blueprint('notes', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")

@notes.route('/notes', methods=['GET', 'POST'])
def my_route():

# 	# if not logged in
# 	username = request.args.get("username")
# 	if username is None: 
# 		if "username" not in session:
# 			return redirect(url_for("index.index_route"))
# 		username = session['username']


	if request.method == 'GET':
		if len(request.args) == 0:
			return render_template("index.html", name="notes")

		#print 'GETTING'
		content = {}
		note_id = request.args['note_id']

		if note_id == '1':
			print 'note id is 1'
			cur = mysql.connection.cursor()
			cur.execute("SELECT note_id,content,time_stamp, is_note, is_instruction, is_image FROM Notes  ORDER BY note_id DESC LIMIT 1;")
			content = cur.fetchone()
			print content

		else:
			print 'note id is greater than 1'
			cur = mysql.connection.cursor()
			cur.execute("SELECT note_id,content,time_stamp, is_note, is_instruction, is_image FROM Notes WHERE note_id = '"+note_id+"'")
			content = cur.fetchone()
			print content

		if content is None:
			return jsonify(successful=False)
		else:
			return jsonify(successful=True, content=content[1], time_stamp=content[2],note_id=content[0], is_note=content[3], is_instruction=content[4], is_snapshot=content[5])


	if request.method == 'POST':
		#print 'POSTING'
		#print request.data

		data = ast.literal_eval(request.data)

		if(data['messageTitle'] == ""):
			data['messageTitle'] = "no title"

		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO Notes (is_note, is_instruction, is_image, title, time_stamp, content) VALUES (%s, %s, %s, %s, %s, %s)", [ True if data['isNote'] == 'true' else False, True if data['isInstruction'] == 'true' else False, True if data['isImage'] == 'true' else False, data['messageTitle'], data['messageTime'], data['messageContent']])
		mysql.connection.commit()

		cur.execute("SELECT note_id FROM Notes WHERE content = %s", [data['messageContent']])
		recent_note_id = max(cur.fetchall())
		
		return jsonify(note_id=recent_note_id) 

	return render_template("index.html", name="notes")
