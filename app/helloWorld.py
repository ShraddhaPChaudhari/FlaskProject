from flask import Flask
app=Flask(__name__) #current module/app name

@app.route("/") #URL Routing/URL creation
@app.route("/contact")
def hello():  #function
    return "Hello world!"  #return-to print on the browser

@app.route("/about")
def hellos():
    return "Hello Shraddha!"

if __name__ == "__main__": #to run on the browser
    app.run()
