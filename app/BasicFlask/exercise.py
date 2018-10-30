from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name=",Dhiraj"
    a="Daneil"
    a1="hello i m Daneil"
    a3="Amar"
    lst=['Tiger','Zinda','hai']
    return render_template('tmp1.html',name1=name,name2=a,name3=a1,name4=lst,name5=a3)

@app.route('/new')
def index1():
    user={'username':'Dhiraj'}
    posts = [
        {
            'author':{'username':'Daneil'},
            'body':'Beautiful day in shrilanka'
            },
        {
            'author':{'username':'Amar'},
            'body':'Tiger Zinda Hai'
            }
        ]
    return render_template('tmp1.html',user=user,posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
