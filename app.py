from flask import Flask
from flask import render_template,redirect,url_for,abort
from flask import request
from flask import make_response

app = Flask(__name__)
app.config.update
({
    'SECRET_KEY':'a random string'
})
#app.config.from_pyfile('path/to/config.py')

#page = request.args.get('page')
#per_page = request.args.get('per_page')


@app.route('/')
def index():
#    return redirect(url_for('user_index',username='default'))
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)

@app.route('/user/<username>')
def user_index(username):
#    resp = make_response(render_template('user_index.html',username=username))
#    resp.set_cookie('username',username)
#    return resp
    if username == 'invalid':
        abort(404)
    return render_template('user_index.html',username=username)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
