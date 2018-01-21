from flask import Flask
from flask import render_template, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/simple_db'
db=SQLAlchemy(app)

class File(db.Model):
	__tablename__ = 'files'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	created_time = db.Column(db.DateTime)
	category_id = db.Column(db.Integer, db.ForeignKey(categories.id))
	content = db.Column(db.Text)
	category = db.relationship('Category')
	def __init__(self, title, created_time, category, content):
		self.title = title
		self.created_time = created_time
		self.category = category
		self.content = content
	
class Category(db.Model):
	__tablename__ = 'categories'
	id = db.Column(db.Integer)
	name = db.Column(db.String(80))
	files = db.relationship('File')
	def __init__(self, name):
		self.name = name

@app.route('/')
def index():
	filelist = File.query.all()
	return render_template('index.html', filelist=filelist)

@app.route('/files/<file_id>')
def file(file_id):
	filecontent = File.query.filter_by(file_id)
	if not filecontent:
		abort(404)
	else:
		return render_template('file.html', filecontent=filecontent)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404

if __name__ == "__main__":
	app.run()