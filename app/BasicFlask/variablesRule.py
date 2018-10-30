from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return 'hello'

@app.route('/hi/<name>')
def hello_name(name):
    return 'hello %s!' % name


@app.route('/hi/<int:name>')
def hello_name1(name):
    return 'hello %i!' % name


@app.route('/hi/<float:name>')
def hello_name2(name):
    return 'hello %f!' % name

if __name__ == '__main__':
    app.run(debug = True)
