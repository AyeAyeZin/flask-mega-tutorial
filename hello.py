from flask import Flask
app=Flask(__name__)
@app.route("/")
@app.route("templ.html")
def index():
    return "Hello World"
def index():
    return "This is index"
if __name__=="__main__":
    app.run()
