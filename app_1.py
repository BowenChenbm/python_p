from flask import Flask
from flask import render_template, abort
import os
import json

app = Flask(__name__)
filespath = '/home/shiyanlou/files'

class File(object):
	def __init__(self):
		self._files = self.__get_filedir()
	def __get_filedir(self):
		filespath = '/home/shiyanlou/files'
		filelist = [ file for file in os.listdir(filespath) ]
		file_dirs = {}
		for file in iter(filelist):
			with open('/'.join([filespath,file]),'r') as jfile:
				file_dirs[file] = json.loads(jfile.read())
		return file_dirs
	def get_filetitles(self):
		return [fileitm.title for fileitem in self._files.values()]
	def get_filecontent_byfilename(self, filename):
		return self._files.get(filename)

filefile = File()

@app.route('/')
def index():
	return render_template('index.html', filelist=filefile.get_filetitles)

@app.route('/files/<filename>')
def file(filename):
	filecontent = filefile.get_filecontent_byfilename(filename)
	if not filecontent:
		abort(404)
	else:
		return render_template('file.html', filecontent=filecontent)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404

if __name__ == "__main__":
	app.run()