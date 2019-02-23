from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "hello...."

@app.route("/home")
def home():
    return "My Home page"    

if(__name__=="__main__"):
    app.run()


