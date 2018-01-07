from flask import Flask
from flask import render_template,redirect,url_for

app = Flask(__name__)
app.config.update
({
    'SECRET_KEY':'a random string'
})
#app.config.from_pyfile('path/to/config.py')

@app.route('/')
def index():
    return redirect(url_for('user_index',username='default'))

@app.route('/user/<username>')
def user_index(username):
    return render_template('user_index.html',username=username)

if __name__ == '__main__':
    app.run()
