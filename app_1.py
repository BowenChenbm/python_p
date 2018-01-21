from flask import Flask
from flask import render_template
import os
import json

app = Flask(__name__)
filespath = '/home/shiyanlou/files'

@app.route('/')
def index():
	filelist = [file for file in os.listdir(filespath)]
	file_dirs = {}
	for file in iter(filelist):
		with open('/'.join([filespath, file]), 'r') as jfile:
			file_dirs[file] = json.loads(jfile.read())
	return render_template('index.html', filelist=file_dirs)

@app.route('/files/<filename>')
def file(filename):
	filename_json = '.'.join([filename,'json'])
	if filename_json in [file for file in os.listdir(filespath)]:
		with open('/'.join([filespath, filename_json]),'r') as jfile:
			file_content = json.loads(jfile.read())
		return render_template('file.html', filecontent=file_content)
	else:
		return render_template('404.html'), 404

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404

if __name__ == "__main__":
	app.run()