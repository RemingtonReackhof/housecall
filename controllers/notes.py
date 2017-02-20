from flask import *
from extensions import mysql
from flask import Flask, session, redirect, url_for, escape, request, flash
import hashlib
import uuid
import ast


notes = Blueprint('notes', __name__, template_folder='templates') #, url_prefix="/04d8ee3a8730446aa2b4/pa3")

@notes.route('/notes/<note_id>', methods=['GET'])
def get_note():
	print 'in here!'
	return jsonify(hello='world')



@notes.route('/notes', methods=['GET', 'POST'])
def my_route():

	if request.method == 'GET':
		print 'GETTING'
		content = {}
		note_id = request.args['note_id']

		if note_id == '1':
			print 'note id is 1'
			cur = mysql.connection.cursor()
			cur.execute("SELECT note_id,content,time_stamp FROM eecs481.Notes  ORDER BY note_id DESC LIMIT 1;")
			content = cur.fetchone()
			print content

		else:
			print 'note id is greater than 1'
			cur = mysql.connection.cursor()
			cur.execute("SELECT note_id,content,time_stamp FROM eecs481.Notes WHERE note_id = '"+note_id+"'")
			content = cur.fetchone()
			print content

		if content is None:
			return jsonify(successful=False)
		else:
			return jsonify(successful=True, content=content[1], time_stamp=content[2],note_id=content[0])


	if request.method == 'POST':
		print 'POSTING'
		print request.data

		data = ast.literal_eval(request.data)

		if(data['messageTitle'] == ""):
			data['messageTitle'] = "no title"

		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO eecs481.Notes (is_note, is_instruction, is_snapshot, title, time_stamp, content) VALUES (%s, %s, %s, %s, %s, %s)", [ True if data['isNote'] == 'true' else False, True if data['isInstruction'] == 'true' else False, True if data['isSnapshot'] == 'true' else False, data['messageTitle'], data['messageTime'], data['messageContent']])
		mysql.connection.commit()

		cur.execute("SELECT note_id FROM eecs481.Notes WHERE content = %s", [data['messageContent']])
		recent_note_id = max(cur.fetchall())
		
		return jsonify(note_id=recent_note_id) 

	return render_template("index.html", name="notes")