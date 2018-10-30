from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name="python workshop"
    lst=['shraddha','shiva,']
    dictionary={'abc':'ABC','xyz':'XYZ','pqr':'PQR'}
    tup=('a','b','c',1999)
    return render_template('tmp.html',name1=name,name2=lst,name3=dictionary,name4=tup)


if __name__ == '__main__':
    app.run(debug=True)



