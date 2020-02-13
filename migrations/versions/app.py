from flask import Flask,render_template,request

def bootstrap():
    app = Flask(__name__)

    @app.route("/home")
    def home():
        return "Home Page"   
    def showname():
        name = request.args.get("name",default=None,type=None)
        return f"Name:{name}"

    @app.route("/name")
    @app.route("/name/<name>")
    def showname_param(name= None):
        
        if name:
            return name
        return "Nome não inserido !"

app = bootstrap()
app.run(debug=True,host='127.0.0.1',port=8080)