from flask import Flask

app = Flask(__name__)
app.config.update
({
    'SECRET_KEY':'a random string'
})
app.config.from_pyfile('path/to/config.py')
@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
